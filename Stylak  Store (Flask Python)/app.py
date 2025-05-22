from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(2), nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Product {self.name} ({self.size})>"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship('Product', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f"<Order {self.id}: {self.quantity}×{self.product.name}>"

@app.route('/')
def index():
    search = request.args.get('search', '')
    size_filter = request.args.get('size')
    sort = request.args.get('sort')

    products = Product.query

    if search:
        products = products.filter(Product.name.ilike(f'%{search}%'))
    if size_filter:
        products = products.filter(Product.size == size_filter)
    if sort == 'asc':
        products = products.order_by(Product.price.asc())
    elif sort == 'desc':
        products = products.order_by(Product.price.desc())

    return render_template('index.html', products=products.all())

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/buy', methods=['POST'])
def buy():
    import json

    items_json = request.form.get('items')
    if not items_json:
        flash('No items received.', 'danger')
        return redirect(url_for('cart'))

    try:
        items = json.loads(items_json)  
    except Exception:
        flash('Invalid cart data.', 'danger')
        return redirect(url_for('cart'))

    for item in items:
        product_id = int(item['id'])
        qty = int(item['quantity'])
        size = item.get('size') 

        product = Product.query.get(product_id)
        if not product or qty > product.stock:
            flash(f'Error: Not enough stock for {product.name} ({product.size})', 'danger')
            return redirect(url_for('cart'))

    for item in items:
        product_id = int(item['id'])
        qty = int(item['quantity'])

        product = Product.query.get(product_id)
        product.stock -= qty

        order = Order(product_id=product_id, quantity=qty)
        db.session.add(order)

    db.session.commit()
    flash('Purchase completed for all items in your cart!', 'success')
    return redirect(url_for('orders'))

@app.route('/orders')
def orders():
    orders = Order.query.order_by(Order.timestamp.desc()).all()
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)

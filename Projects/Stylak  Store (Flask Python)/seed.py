from app import app, db, Product

def seed():
    items = [
        {'name': 'Shirt',  'price': 20.0},
        {'name': 'Pants',  'price': 30.0},
        {'name': 'Blouse', 'price': 25.0},
        {'name': 'Jacket', 'price': 50.0},
        {'name': 'Hoodie', 'price': 45.0},
    ]
    sizes = ['S', 'M', 'L']
    for item in items:
        for size in sizes:
            p = Product(
                name=item['name'],
                price=item['price'],
                size=size,
                stock=1000
            )
            db.session.add(p)
    db.session.commit()
    print("Seed data inserted.")

if __name__ == '__main__':

    with app.app_context():
        seed()

let cart = JSON.parse(localStorage.getItem('cart')) || [];

function saveCart() {
  localStorage.setItem('cart', JSON.stringify(cart));
}

function addToCart(product) {
  const existing = cart.find(item => item.id === product.id && item.size === product.size);
  if (existing) {
    if (existing.quantity < product.stock) {
      existing.quantity++;
    } else {
      alert('Cannot add more than stock available');
      return;
    }
  } else {
    cart.push({ ...product, quantity: 1 });
  }
  saveCart();
  if (window.location.pathname === '/cart') {
    renderCart();
  }
  alert(`${product.name} (${product.size}) added to cart.`);
}

function renderCart() {
  const container = document.getElementById('cart-items');
  if (!container) return;

  container.innerHTML = '';
  if (cart.length === 0) {
    container.innerHTML = '<p>Your cart is empty.</p>';
    return;
  }

  cart.forEach(item => {
    const div = document.createElement('div');
    div.className = 'd-flex justify-content-between align-items-center mb-3 p-2 border rounded';
    div.innerHTML = `
      <span><strong>${item.name}</strong> (${item.size}) - $${item.price.toFixed(2)}</span>
      <div class="d-flex align-items-center">
        <button class="btn btn-sm btn-outline-secondary me-1" onclick="changeQuantity(${item.id}, '${item.size}', -1)">-</button>
        <span class="mx-2">${item.quantity}</span>
        <button class="btn btn-sm btn-outline-secondary me-2" onclick="changeQuantity(${item.id}, '${item.size}', 1)">+</button>
        <button class="btn btn-sm btn-danger" onclick="removeItem(${item.id}, '${item.size}')">Remove</button>
      </div>
    `;
    container.appendChild(div);
  });
}

function changeQuantity(id, size, delta) {
  const item = cart.find(i => i.id === id && i.size === size);
  if (!item) return;

  const newQty = item.quantity + delta;
  if (newQty <= 0) {
    removeItem(id, size);
  } else if (newQty > item.stock) {
    alert('Cannot exceed available stock.');
  } else {
    item.quantity = newQty;
  }

  saveCart();
  renderCart();
}

function removeItem(id, size) {
  cart = cart.filter(i => !(i.id === id && i.size === size));
  saveCart();
  renderCart();
}

const checkoutBtn = document.getElementById('checkout-btn');
if (checkoutBtn) {
  checkoutBtn.addEventListener('click', () => {
    if (cart.length === 0) {
      alert('Your cart is empty.');
      return;
    }

    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/buy';

    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'items';
    input.value = JSON.stringify(cart.map(item => ({
      id: item.id,
      quantity: item.quantity,
      size: item.size
    })));
    form.appendChild(input);

    localStorage.removeItem('cart');
    cart = [];

    document.body.appendChild(form);
    form.submit();
  });
}

document.querySelectorAll('.add-to-cart').forEach(btn => {
  btn.addEventListener('click', () => {
    const product = {
      id: parseInt(btn.dataset.id),
      name: btn.dataset.name,
      size: btn.dataset.size,
      price: parseFloat(btn.dataset.price),
      stock: parseInt(btn.dataset.stock)
    };
    addToCart(product);
  });
});

if (window.location.pathname === '/cart') {
  renderCart();
}

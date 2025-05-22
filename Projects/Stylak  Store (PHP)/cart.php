<?php
// cart.php
require 'config.php';
?>
<?php include 'templates/header.php'; ?>
<div class="container py-4">
    <h2>Your Cart</h2>
    <div id="cart-items"></div>
    <div class="mt-4">
        <button id="checkout-btn" class="btn btn-success">Checkout</button>
        <a href="index.php" class="btn btn-secondary ms-2">Continue Shopping</a>
    </div>
</div>
<?php include 'templates/footer.php'; ?>

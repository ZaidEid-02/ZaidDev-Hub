<?php
// buy.php
require 'config.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $items = json_decode($_POST['items'], true);
    if (!$items) {
        header('Location: cart.php');
        exit;
    }
    foreach ($items as $item) {
        $stmt = $pdo->prepare('SELECT * FROM products WHERE id=?');
        $stmt->execute([$item['id']]);
        $product = $stmt->fetch(PDO::FETCH_ASSOC);
        if (!$product || $item['quantity'] > $product['stock']) {
            header('Location: cart.php');
            exit;
        }
    }
    foreach ($items as $item) {
        $pdo->prepare('UPDATE products SET stock = stock - ? WHERE id = ?')
            ->execute([$item['quantity'], $item['id']]);
        $pdo->prepare('INSERT INTO orders (product_id, quantity) VALUES (?,?)')
            ->execute([$item['id'], $item['quantity']]);
    }
    header('Location: orders.php');
    exit;
}
header('Location: cart.php');
exit;
?>
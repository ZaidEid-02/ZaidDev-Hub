<?php
// orders.php
require 'config.php';
$stmt = $pdo->query('SELECT o.id, p.name, p.size, o.quantity, o.timestamp 
                     FROM orders o JOIN products p ON o.product_id = p.id 
                     ORDER BY o.timestamp DESC');
$orders = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<?php include 'templates/header.php'; ?>
<div class="container py-4">
    <h2>Order History</h2>
    <?php if ($orders): ?>
    <table class="table">
        <thead><tr><th>ID</th><th>Product</th><th>Size</th><th>Quantity</th><th>Date</th></tr></thead>
        <tbody>
        <?php foreach ($orders as $o): ?>
        <tr>
            <td><?= $o['id'] ?></td>
            <td><?= htmlspecialchars($o['name']) ?></td>
            <td><?= $o['size'] ?></td>
            <td><?= $o['quantity'] ?></td>
            <td><?= $o['timestamp'] ?></td>
        </tr>
        <?php endforeach; ?>
        </tbody>
    </table>
    <?php else: ?>
    <p>You have no past orders.</p>
    <?php endif; ?>
</div>
<?php include 'templates/footer.php'; ?>

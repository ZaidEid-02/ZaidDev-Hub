<?php
// config.php
session_start();

define('DB_HOST', 'localhost');
define('DB_NAME', 'store');
define('DB_USER', 'root');
define('DB_PASS', '');

try {
    $pdo = new PDO("mysql:host=" . DB_HOST, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    // Create database if not exists
    $pdo->exec("CREATE DATABASE IF NOT EXISTS " . DB_NAME);
    $pdo->exec("USE " . DB_NAME);
    // Create tables
    $pdo->exec("CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        size CHAR(2) NOT NULL,
        stock INT NOT NULL DEFAULT 0
    ) ENGINE=InnoDB;");
    $pdo->exec("CREATE TABLE IF NOT EXISTS orders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
    ) ENGINE=InnoDB;");
    // Seed data if table empty
    $count = $pdo->query('SELECT COUNT(*) FROM products')->fetchColumn();
    if ($count == 0) {
        $items = [
            ['Shirt', 20.00],
            ['Pants', 30.00],
            ['Blouse', 25.00],
            ['Jacket', 50.00],
            ['Hoodie', 45.00],
        ];
        $sizes = ['S', 'M', 'L'];
        $stmt = $pdo->prepare('INSERT INTO products (name, price, size, stock) VALUES (?, ?, ?, 1000)');
        foreach ($items as $item) {
            foreach ($sizes as $size) {
                $stmt->execute([$item[0], $item[1], $size]);
            }
        }
    }
} catch (PDOException $e) {
    die('Database error: ' . $e->getMessage());
}
?>
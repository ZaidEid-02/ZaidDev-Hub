<?php
// index.php
require 'config.php';

$search = $_GET['search'] ?? '';
$size_filter = $_GET['size'] ?? '';
$sort = $_GET['sort'] ?? '';

// Build SQL query
$sql = 'SELECT * FROM products WHERE 1';
$params = [];
if ($search) {
    $sql .= ' AND name LIKE ?';
    $params[] = "%$search%";
}
if ($size_filter) {
    $sql .= ' AND size = ?';
    $params[] = $size_filter;
}
if ($sort === 'asc') {
    $sql .= ' ORDER BY price ASC';
} elseif ($sort === 'desc') {
    $sql .= ' ORDER BY price DESC';
}
$stmt = $pdo->prepare($sql);
$stmt->execute($params);
$products = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<?php include 'templates/header.php'; ?>

<!-- Hero Section: Logo and Store Title -->
<section class="hero">
  <img src="static/images/logo.png"
       alt="Stylak Store Logo"
       class="hero-logo">
  <h1 class="hero-title">Stylak Store</h1>
  <p class="hero-subtitle">The best place for your style essentials</p>
  <!-- Changed href to scroll to products section -->
  <a href="#products" class="btn btn-light">Shop Now</a>
</section>

<!-- Search & Filters -->
<div class="container py-4">
    <form method="get" class="row g-3 align-items-end">
        <div class="col-md-4">
            <label for="search" class="form-label">Search by Name</label>
            <input type="text" name="search" id="search" class="form-control" value="<?= htmlspecialchars($search) ?>">
        </div>
        <div class="col-md-2">
            <label for="size" class="form-label">Size</label>
            <select name="size" id="size" class="form-select">
                <option value="">All</option>
                <?php foreach (['S','M','L'] as $s): ?>
                <option value="<?= $s ?>" <?= $size_filter==$s ? 'selected' : '' ?>><?= $s ?></option>
                <?php endforeach; ?>
            </select>
        </div>
        <div class="col-md-2">
            <label for="sort" class="form-label">Sort by Price</label>
            <select name="sort" id="sort" class="form-select">
                <option value="">None</option>
                <option value="asc" <?= $sort=='asc' ? 'selected' : '' ?>>Low to High</option>
                <option value="desc" <?= $sort=='desc' ? 'selected' : '' ?>>High to Low</option>
            </select>
        </div>
        <div class="col-md-2">
            <button type="submit" class="btn btn-primary w-100">Apply</button>
        </div>
        <div class="col-md-2">
            <a href="index.php" class="btn btn-secondary w-100">Reset</a>
        </div>
    </form>
</div>

<!-- Products Grid -->
<div class="container py-4" id="products">
    <div class="row">
        <?php foreach ($products as $product): ?>
        <div class="col-md-4 mb-4">
            <div class="card h-100 shadow-sm product-card">
                <img src="static/images/<?= strtolower($product['name']) ?>.png" alt="<?= htmlspecialchars($product['name']) ?>"
                     class="card-img-top p-4" style="object-fit:contain; height:200px;">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title"><?= htmlspecialchars($product['name']) ?> - <?= $product['size'] ?></h5>
                    <p class="card-text">Price: $<?= number_format($product['price'],2) ?></p>
                    <p class="card-text">Stock: <?= $product['stock'] ?></p>
                    <button class="btn btn-primary mt-auto add-to-cart"
                            data-id="<?= $product['id'] ?>"
                            data-name="<?= htmlspecialchars($product['name']) ?>"
                            data-size="<?= $product['size'] ?>"
                            data-price="<?= $product['price'] ?>"
                            data-stock="<?= $product['stock'] ?>">
                        Add to Cart
                    </button>
                </div>
            </div>
        </div>
        <?php endforeach; ?>
    </div>
</div>

<?php include 'templates/footer.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stylak Store</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Bootstrap Icons -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">
  <!-- ستايل الموقع -->
  <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <!-- شعار الموقع -->
      <a class="navbar-brand d-flex align-items-center" href="index.php">
        <img src="static/images/logo.png" alt="Stylak Store" height="75" class="me-2">
        <span class="fs-2 fw-bold">Stylak Store</span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
              data-bs-target="#navbarNav" aria-controls="navbarNav"
              aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link d-flex align-items-center" href="index.php">
              <i class="bi bi-house-fill fs-4 me-1"></i> Home
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link d-flex align-items-center" href="cart.php">
              <i class="bi bi-cart-fill fs-4 me-1"></i> Cart
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link d-flex align-items-center" href="orders.php">
              <i class="bi bi-clock-history fs-4 me-1"></i> Order History
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

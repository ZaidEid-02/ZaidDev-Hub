# sales_management_system.py

# تخزين سجلات المبيعات في قاموس يحتوي على معرّف البيع كمفتاح
sales_data = {
    1: {"product_name": "Laptop Dell Inspiron", "quantity_sold": 2, "sale_amount": 1200.0, "sale_date": "2025-05-01"},
    2: {"product_name": "iPhone 14 Pro", "quantity_sold": 1, "sale_amount": 1000.0, "sale_date": "2025-05-03"},
    3: {"product_name": "Samsung Smart TV 55\"", "quantity_sold": 1, "sale_amount": 650.0, "sale_date": "2025-05-04"},
    4: {"product_name": "Canon EOS 4000D Camera", "quantity_sold": 3, "sale_amount": 900.0, "sale_date": "2025-05-06"},
    5: {"product_name": "Gaming Mouse Logitech G502", "quantity_sold": 4, "sale_amount": 200.0, "sale_date": "2025-05-07"},
    6: {"product_name": "HP Laser Printer M15w", "quantity_sold": 2, "sale_amount": 180.0, "sale_date": "2025-05-08"},
    7: {"product_name": "Bluetooth Speaker JBL", "quantity_sold": 5, "sale_amount": 250.0, "sale_date": "2025-05-10"},
    8: {"product_name": "Asus ROG Gaming Laptop", "quantity_sold": 1, "sale_amount": 1500.0, "sale_date": "2025-05-11"},
    9: {"product_name": "Apple Watch Series 9", "quantity_sold": 2, "sale_amount": 700.0, "sale_date": "2025-05-12"},
    10: {"product_name": "Xiaomi Redmi Note 13", "quantity_sold": 3, "sale_amount": 480.0, "sale_date": "2025-05-13"}
}

# دالة لإضافة سجل بيع جديد
def add_sale():
    # إدخال معرّف البيع مع التحقق من عدم تكراره
    while True:
        try:
            sale_id = int(input("Enter Sale ID: "))
            if sale_id in sales_data:
                print("❌ Sale ID already exists. Please enter a unique ID.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Sale ID must be a number.")

    # إدخال اسم المنتج والتحقق من عدم كونه فارغًا
    product_name = input("Enter Product Name: ").strip()
    if not product_name:
        print("❌ Product name cannot be empty.")
        return

    # إدخال الكمية المباعة والتحقق من صحتها
    while True:
        try:
            quantity_sold = int(input("Enter Quantity Sold: "))
            if quantity_sold < 0:
                print("❌ Quantity must be non-negative.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Quantity must be a number.")

    # إدخال قيمة البيع والتحقق من صحتها
    while True:
        try:
            sale_amount = float(input("Enter Sale Amount (in JOD): "))
            if sale_amount < 0:
                print("❌ Amount must be non-negative.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid amount (e.g., 120.5).")

    # إدخال تاريخ البيع
    sale_date = input("Enter Sale Date (YYYY-MM-DD): ").strip()
    if not sale_date:
        print("❌ Sale date cannot be empty.")
        return

    # إضافة السجل إلى القاموس
    sales_data[sale_id] = {
        "product_name": product_name,
        "quantity_sold": quantity_sold,
        "sale_amount": sale_amount,
        "sale_date": sale_date
    }
    print("✅ Sale record added successfully!")

# دالة لعرض جميع سجلات المبيعات
def view_sales():
    if not sales_data:
        print("No sales records found.")
    else:
        print("\n----- Sales Records -----")
        # عرض كل سجل مع تنسيق مناسب
        for idx, (sale_id, record) in enumerate(sales_data.items(), start=1):
            print(f"\n{idx}. Sale ID: {sale_id}")
            for key, value in record.items():
                if key == "sale_amount":
                    print(f"   {key.replace('_', ' ').title()}: {value} JOD")
                else:
                    print(f"   {key.replace('_', ' ').title()}: {value}")
        print("--------------------------")

# دالة للبحث عن سجل بيع حسب معرّف البيع
def search_sale():
    try:
        sale_id = int(input("Enter Sale ID to search: "))
        if sale_id in sales_data:
            print(f"\nSale ID: {sale_id}")
            for key, value in sales_data[sale_id].items():
                if key == "sale_amount":
                    print(f"{key.replace('_', ' ').title()}: {value} JOD")
                else:
                    print(f"{key.replace('_', ' ').title()}: {value}")
        else:
            print("Sale record not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# دالة لحذف سجل بيع بناءً على المعرّف
def delete_sale():
    try:
        sale_id = int(input("Enter Sale ID to delete: "))
        if sale_id in sales_data:
            del sales_data[sale_id]
            print("Sale record deleted.")
        else:
            print("Sale record not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# دالة لتحديث معلومات سجل بيع موجود
def update_sale():
    try:
        sale_id = int(input("Enter Sale ID to update: "))
        if sale_id not in sales_data:
            print("Sale record not found.")
            return

        record = sales_data[sale_id]
        print("Leave blank to keep existing value.")

        # تحديث اسم المنتج (يمكن تركه كما هو)
        new_name = input(f"Product Name ({record['product_name']}): ").strip()
        if not new_name:
            new_name = record['product_name']

        # تحديث الكمية المباعة
        while True:
            new_quantity = input(f"Quantity Sold ({record['quantity_sold']}): ").strip()
            if not new_quantity:
                new_quantity = record['quantity_sold']
                break
            try:
                new_quantity = int(new_quantity)
                if new_quantity < 0:
                    print("❌ Quantity must be non-negative.")
                    continue
                break
            except ValueError:
                print("❌ Invalid input. Quantity must be a number.")

        # تحديث قيمة البيع
        while True:
            new_amount = input(f"Sale Amount ({record['sale_amount']} JOD): ").strip()
            if not new_amount:
                new_amount = record['sale_amount']
                break
            try:
                new_amount = float(new_amount)
                if new_amount < 0:
                    print("❌ Amount must be non-negative.")
                    continue
                break
            except ValueError:
                print("❌ Invalid input. Please enter a valid amount (e.g., 120.5).")

        # تحديث تاريخ البيع
        new_date = input(f"Sale Date ({record['sale_date']}): ").strip()
        if not new_date:
            new_date = record['sale_date']

        # تحديث السجل في القاموس
        record['product_name'] = new_name
        record['quantity_sold'] = new_quantity
        record['sale_amount'] = new_amount
        record['sale_date'] = new_date

        print("✅ Sale record updated.")

    except ValueError:
        print("❌ Invalid input. Sale ID must be a number.")

# دالة لعرض الإحصائيات الخاصة بالمبيعات
def show_analytics():
    while True:
        print("""
        ----- Sales Analytics Options -----
        1. Total Sales Amount
        2. Average Sale Amount
        3. Best-Selling Product (by quantity)
        4. Show All Analytics
        5. Return to Main Menu
        -----------------------------------
        """)
        choice = input("Select an option (1-5): ")

        # إجمالي المبيعات
        if choice == '1':
            total_sales = sum(record['sale_amount'] for record in sales_data.values())
            print(f"1. Total Sales Amount: {total_sales} JOD")

        # متوسط المبيعات
        elif choice == '2':
            if sales_data:
                avg_sales = sum(r['sale_amount'] for r in sales_data.values()) / len(sales_data)
                print(f"2. Average Sale Amount: {avg_sales:.2f} JOD")
            else:
                print("No sales data available.")

        # المنتج الأكثر مبيعًا
        elif choice == '3':
            if sales_data:
                max_quantity = max(record['quantity_sold'] for record in sales_data.values())
                best_selling_products = [record for record in sales_data.values() if record['quantity_sold'] == max_quantity]

                print("3. Best-Selling Product(s):")
                for product in best_selling_products:
                    print(f"   - {product['product_name']} ({product['quantity_sold']} units)")
            else:
                print("No sales data available.")

        # جميع الإحصائيات معًا
        elif choice == '4':
            if sales_data:
                total_sales = sum(r['sale_amount'] for r in sales_data.values())
                avg_sales = total_sales / len(sales_data)
                max_quantity = max(record['quantity_sold'] for record in sales_data.values())
                best_selling_products = [record for record in sales_data.values() if record['quantity_sold'] == max_quantity]

                print("\n----- Full Analytics Report -----")
                print(f"1. Total Sales Amount: {total_sales} JOD")
                print(f"2. Average Sale Amount: {avg_sales:.2f} JOD")
                print(f"3. Best-Selling Product(s):")
                for product in best_selling_products:
                    print(f"   {product['product_name']} ({product['quantity_sold']} units)")
                print("---------------------------------")
            else:
                print("No sales data available.")

        # العودة للقائمة الرئيسية
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# دالة القائمة الرئيسية التي تسمح بالتنقل بين الخيارات
def menu():
    while True:
        print("""
        ----- Sales Management System -----
        1. Add Sale
        2. View Sales
        3. Search Sale
        4. Delete Sale
        5. Update Sale
        6. Show Analytics
        7. Exit
        -----------------------------------
        """)
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_sale()
        elif choice == '2':
            view_sales()
        elif choice == '3':
            search_sale()
        elif choice == '4':
            delete_sale()
        elif choice == '5':
            update_sale()
        elif choice == '6':
            show_analytics()
        elif choice == '7':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# تنفيذ البرنامج إذا كان هذا هو الملف الرئيسي
if __name__ == '__main__':
    menu()

from src.database import create_client, get_all_clients, get_client, update_client, delete_client, create_employee, get_all_employees, get_employee, update_employee, delete_employee, create_provider, get_all_providers, get_provider, update_provider, delete_provider, create_product, get_all_products, get_product, update_product, delete_product, record_sale, get_all_sales, get_sale, update_sale, delete_sale, record_purchase, get_all_purchases, update_purchase, delete_purchase
from tabulate import tabulate

def employee_menu():
    while True:
        print("""Employee Management
              1. Add Employee
              2. View Employees
              3. Search Employee
              4. Update Employee
              5. Delete Employee
              6. Back to Main Menu""")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter employee name: ")
            role = input("Enter employee role: ")
            create_employee(name, role)
            print("Employee added successfully.")
        elif choice == '2':
            employees = get_all_employees()
            print(tabulate(employees, headers=["ID", "Name", "Role"], tablefmt="grid"))
        elif choice == '3':
            emp_id = input("Enter employee ID to search: ")
            employee = get_employee(emp_id)
            if employee:
                print(tabulate([employee], headers=["ID", "Name", "Role"], tablefmt="grid"))
            else:
                print("Employee not found.")
        elif choice == '4':
            emp_id = input("Enter employee ID to update: ")
            name = input("Enter new name: ")
            role = input("Enter new role: ")
            update_employee(emp_id, name, role)
            print("Employee updated successfully.")
        elif choice == '5':
            emp_id = input("Enter employee ID to delete: ")
            delete_employee(emp_id)
            print("Employee deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def client_menu():
    while True:
        print("""Client Management
              1. Add Client
              2. View Clients
              3. Search Client
              4. Update Client
              5. Delete Client
              6. Back to Main Menu""")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter client name: ")
            email = input("Enter client email: ")
            phone = input("Enter client phone: ")
            create_client(name, email, phone)
            print("Client added successfully.")
        elif choice == '2':
            clients = get_all_clients()
            print(tabulate(clients, headers=["ID", "Name", "Email", "Phone"], tablefmt="grid"))
        elif choice == '3':
            client_id = input("Enter client ID to search: ")
            client = get_client(client_id)
            if client:
                print(tabulate([client], headers=["ID", "Name", "Email", "Phone"], tablefmt="grid"))
            else:
                print("Client not found.")
        elif choice == '4':
            client_id = input("Enter client ID to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            update_client(client_id, name, email, phone)
            print("Client updated successfully.")
        elif choice == '5':
            client_id = input("Enter client ID to delete: ")
            delete_client(client_id)
            print("Client deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def provider_menu():
    while True:
        print("""Provider Management
              1. Add Provider
              2. View Providers
              3. Search Provider
              4. Update Provider
              5. Delete Provider
              6. Back to Main Menu""")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter provider name: ")
            email = input("Enter provider email: ")
            phone = input("Enter provider phone: ")
            field = input("Enter provider field: ")
            create_provider(name, email, phone, field)
            print("Provider added successfully.")
        elif choice == '2':
            providers = get_all_providers()
            print(tabulate(providers, headers=["ID", "Name", "Email", "Phone", "Field"], tablefmt="grid"))
        elif choice == '3':
            provider_id = input("Enter provider ID to search: ")
            provider = get_provider(provider_id)
            if provider:
                print(tabulate([provider], headers=["ID", "Name", "Email", "Phone", "Field"], tablefmt="grid"))
            else:
                print("Provider not found.")
        elif choice == '4':
            provider_id = input("Enter provider ID to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            field = input("Enter new field: ")
            update_provider(provider_id, name, email, phone, field)
            print("Provider updated successfully.")
        elif choice == '5':
            provider_id = input("Enter provider ID to delete: ")
            delete_provider(provider_id)
            print("Provider deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def product_menu():
    while True:
        print("""Product Management
              1. Add Product
              2. View Products
              3. Search Product
              4. Update Product
              5. Delete Product
              6. Back to Main Menu""")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            provider_id = int(input("Enter provider ID: "))
            create_product(name, description, price, stock, provider_id)
            print("Product added successfully.")
        elif choice == '2':
            products = get_all_products()
            print(tabulate(products, headers=["ID", "Name", "Description", "Price", "Stock", "Provider ID"], tablefmt="grid"))
        elif choice == '3':
            product_id = input("Enter product ID to search: ")
            product = get_product(product_id)
            if product:
                print(tabulate([product], headers=["ID", "Name", "Description", "Price", "Stock", "Provider ID"], tablefmt="grid"))
            else:
                print("Product not found.")
        elif choice == '4':
            product_id = input("Enter product ID to update: ")
            name = input("Enter new name: ")
            description = input("Enter new description: ")
            price = float(input("Enter new price: "))
            stock = int(input("Enter new stock: "))
            provider_id = int(input("Enter new provider ID: "))
            update_product(product_id, name, description, price, stock, provider_id)
            print("Product updated successfully.")
        elif choice == '5':
            product_id = input("Enter product ID to delete: ")
            delete_product(product_id)
            print("Product deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def sales_menu():
    while True:
        print("""Sales Management
              1. Record Sale
              2. View Sales
              3. Search Sale
              4. Correct Sale
              5. Delete Sale
              6. Back to Main Menu""")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity sold: "))
            record_sale(product_id, quantity)
            print("Sale recorded successfully.")
        elif choice == '2':
            sales = get_all_sales()
            print(tabulate(sales, headers=["ID", "Product ID", "Quantity", "Date"], tablefmt="grid"))
        elif choice == '3':
            sale_id = input("Enter sale ID to search: ")
            sale = get_sale(sale_id)
            if sale:
                print(tabulate([sale], headers=["ID", "Product ID", "Quantity", "Date"], tablefmt="grid"))
            else:
                print("Sale not found.")
        elif choice == '4':
            sale_id = input("Enter sale ID to correct: ")
            product_id = int(input("Enter new product ID: "))
            quantity = int(input("Enter new quantity sold: "))
            update_sale(sale_id, product_id, quantity)
            print("Sale updated successfully.")
        elif choice == '5':
            sale_id = input("Enter sale ID to delete: ")
            delete_sale(sale_id)
            print("Sale deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def purchases_menu():
    while True:
        print("""Purchases Management
              1. Record Purchase
              2. View Purchases
              3. Search Purchase
              4. Correct Purchase
              5. Delete Purchase
              6. Back to Main Menu""")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            provider_id = int(input("Enter provider ID: "))
            product_id = int(input("Enter product ID: "))
            date = input("Enter purchase date (YYYY-MM-DD): ")
            total = float(input("Enter total amount: "))
            record_purchase(provider_id, product_id, date, total)
            print("Purchase recorded successfully.")
        elif choice == '2':
            purchases = get_all_purchases()
            print(tabulate(purchases, headers=["ID", "Provider ID", "Product ID", "Date", "Total"], tablefmt="grid"))
        elif choice == '3':
            purchase_id = input("Enter purchase ID to search: ")
            purchase = get_purchase(purchase_id)
            if purchase:
                print(tabulate([purchase], headers=["ID", "Provider ID", "Product ID", "Date", "Total"], tablefmt="grid"))
            else:
                print("Purchase not found.")
        elif choice == '4':
            purchase_id = input("Enter purchase ID to correct: ")
            provider_id = int(input("Enter new provider ID: "))
            product_id = int(input("Enter new product ID: "))
            date = input("Enter new purchase date (YYYY-MM-DD): ")
            total = float(input("Enter new total amount: "))
            update_purchase(purchase_id, provider_id, product_id, date, total)
            print("Purchase updated successfully.")
        elif choice == '5':
            purchase_id = input("Enter purchase ID to delete: ")
            delete_purchase(purchase_id)
            print("Purchase deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def main():
    while True:
        print("""Welcome to CLInventory System
              1. Manage Employees
              2. Manage Clients
              3. Manage Providers
              4. Manage Products
              5. Manage Sales
              6. Manage Purchases
              7. Exit""")
        choice = input("Select an option (1-7): ")
        if choice == '1':
            employee_menu()
        elif choice == '2':
            client_menu()
        elif choice == '3':
            provider_menu()
        elif choice == '4':
            product_menu()
        elif choice == '5':
            sales_menu()
        elif choice == '6':
            purchases_menu()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
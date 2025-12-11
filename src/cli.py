import src.database
from tabulate import tabulate

def employee_menu():
    while True:
        print("""Employee Management
              1. Add Employee
              2. View Employees
              3. Update Employee
              4. Delete Employee
              5. Back to Main Menu""")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter employee name: ")
            role = input("Enter employee role: ")
            src.database.create_employee(name, role)
            print("Employee added successfully.")
        elif choice == '2':
            employees = database.get_all_employees()
            print(tabulate(employees, headers=["ID", "Name", "Role"], tablefmt="grid"))
        elif choice == '3':
            emp_id = input("Enter employee ID to update: ")
            name = input("Enter new name: ")
            role = input("Enter new role: ")
            src.database.update_employee(emp_id, name, role)
            print("Employee updated successfully.")
        elif choice == '4':
            emp_id = input("Enter employee ID to delete: ")
            src.database.delete_employee(emp_id)
            print("Employee deleted successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

def client_menu():
    while True:
        print("""Client Management
              1. Add Client
              2. View Clients
              3. Update Client
              4. Delete Client
              5. Back to Main Menu""")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter client name: ")
            email = input("Enter client email: ")
            phone = input("Enter client phone: ")
            src.database.create_client(name, email, phone)
            print("Client added successfully.")
        elif choice == '2':
            clients = src.database.get_all_clients()
            print(tabulate(clients, headers=["ID", "Name", "Email", "Phone"], tablefmt="grid"))
        elif choice == '3':
            client_id = input("Enter client ID to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            src.database.update_client(client_id, name, email, phone)
            print("Client updated successfully.")
        elif choice == '4':
            client_id = input("Enter client ID to delete: ")
            src.database.delete_client(client_id)
            print("Client deleted successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

def provider_menu():
    while True:
        print("""Provider Management
              1. Add Provider
              2. View Providers
              3. Update Provider
              4. Delete Provider
              5. Back to Main Menu""")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter provider name: ")
            email = input("Enter provider email: ")
            phone = input("Enter provider phone: ")
            field = input("Enter provider field: ")
            src.database.create_provider(name, email, phone, field)
            print("Provider added successfully.")
        elif choice == '2':
            providers = src.database.get_all_providers()
            print(tabulate(providers, headers=["ID", "Name", "Email", "Phone", "Field"], tablefmt="grid"))
        elif choice == '3':
            provider_id = input("Enter provider ID to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            field = input("Enter new field: ")
            src.database.update_provider(provider_id, name, email, phone, field)
            print("Provider updated successfully.")
        elif choice == '4':
            provider_id = input("Enter provider ID to delete: ")
            src.database.delete_provider(provider_id)
            print("Provider deleted successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

def product_menu():
    while True:
        print("""Product Management
              1. Add Product
              2. View Products
              3. Update Product
              4. Delete Product
              5. Back to Main Menu""")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            provider_id = int(input("Enter provider ID: "))
            src.database.create_product(name, description, price, stock, provider_id)
            print("Product added successfully.")
        elif choice == '2':
            products = src.database.get_all_products()
            print(tabulate(products, headers=["ID", "Name", "Description", "Price", "Stock", "Provider ID"], tablefmt="grid"))
        elif choice == '3':
            product_id = input("Enter product ID to update: ")
            name = input("Enter new name: ")
            description = input("Enter new description: ")
            price = float(input("Enter new price: "))
            stock = int(input("Enter new stock: "))
            provider_id = int(input("Enter new provider ID: "))
            src.database.update_product(product_id, name, description, price, stock, provider_id)
            print("Product updated successfully.")
        elif choice == '4':
            product_id = input("Enter product ID to delete: ")
            src.database.delete_product(product_id)
            print("Product deleted successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

def sales_menu():
    while True:
        print("""Sales Management
              1. Record Sale
              2. View Sales
              3. Back to Main Menu""")
        choice = input("Select an option (1-3): ")
        if choice == '1':
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity sold: "))
            src.database.record_sale(product_id, quantity)
            print("Sale recorded successfully.")
        elif choice == '2':
            sales = src.database.get_all_sales()
            print(tabulate(sales, headers=["ID", "Product ID", "Quantity", "Date"], tablefmt="grid"))
        elif choice == '3':
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
              6. Exit""")
        choice = input("Select an option (1-6): ")
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
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
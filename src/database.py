import sqlite3
from src.config import DB_PATH

def get_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = 1")  # Enable foreign key support
    conn.row_factory = sqlite3.Row  # Enable dictionary-like row access
    return conn

def create_database():
    """Creates tables for the database if they do not exist."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.executescript(
            """CREATE TABLE IF NOT EXISTS Employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    role TEXT
                    );
            CREATE TABLE IF NOT EXISTS Clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT
                    );
            CREATE TABLE IF NOT EXISTS Providers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    field TEXT
                    );
            CREATE TABLE IF NOT EXISTS Products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL,
                    provider_id INTEGER,
                    FOREIGN KEY (provider_id) REFERENCES Providers(id)
                    );
            CREATE TABLE IF NOT EXISTS Sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id INTEGER NOT NULL,
                    product_id INTEGER NOT NULL,
                    employee_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    total REAL NOT NULL,
                    FOREIGN KEY (client_id) REFERENCES Clients(id),
                    FOREIGN KEY (product_id) REFERENCES Products(id),
                    FOREIGN KEY (employee_id) REFERENCES Employees(id)
                    ); 
            CREATE TABLE IF NOT EXISTS Purchases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    provider_id INTEGER NOT NULL,
                    product_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    total REAL NOT NULL,
                    FOREIGN KEY (provider_id) REFERENCES Providers(id),
                    FOREIGN KEY (product_id) REFERENCES Products(id)
                    );
                    """)

def create_employee(name, role):
    """Creates a new employee in the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Employees (name, role) VALUES (?, ?)", (name, role))
        conn.commit()

def get_employee(employee_id):
    """Retrieves a specific employee by ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employees WHERE id = ?", (employee_id,))
        return cursor.fetchone()

def get_all_employees():
    """Retrieves a list of all employees from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employees")
        return cursor.fetchall()

def update_employee(employee_id, name, role):
    """Updates an existing employee's details."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Employees SET name = ?, role = ? WHERE id = ?", (name, role, employee_id))
        conn.commit()

def delete_employee(employee_id):
    """Deletes an employee from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Employees WHERE id = ?", (employee_id,))
        conn.commit()

def create_client(name, email, phone):
    """Creates a new client in the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Clients (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        conn.commit()

def get_client(client_id):
    """Retrieves a specific client by ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Clients WHERE id = ?", (client_id,))
        return cursor.fetchone()

def get_all_clients():
    """Retrieves a list of all clients from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Clients")
        return cursor.fetchall()

def update_client(client_id, name, email, phone):
    """Updates an existing client's details."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Clients SET name = ?, email = ?, phone = ? WHERE id = ?", (name, email, phone, client_id))
        conn.commit()

def delete_client(client_id):
    """Deletes a client from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Clients WHERE id = ?", (client_id,))
        conn.commit()

def create_provider(name, email, phone, field):
    """Creates a new provider to the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Providers (name, email, phone, field) VALUES (?, ?, ?, ?)", (name, email, phone, field))
        conn.commit()

def get_provider(provider_id):
    """Retrieves a specific provider by ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Providers WHERE id = ?", (provider_id,))
        return cursor.fetchone()

def get_all_providers():
    """Retrieves a list of all providers from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Providers")
        return cursor.fetchall()

def update_provider(provider_id, name, email, phone, field):
    """Updates an existing provider's details."""    
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Providers SET name = ?, email = ?, phone = ?, field = ? WHERE id = ?", (name, email, phone, field, provider_id))
        conn.commit()

def delete_provider(provider_id):
    """Deletes a provider from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Providers WHERE id = ?", (provider_id,))
        conn.commit()

def create_product(name, description, price, stock, provider_id):
    """Creates a new product in the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Products (name, description, price, stock, provider_id) VALUES (?, ?, ?, ?, ?)", (name, description, price, stock, provider_id))
        conn.commit()

def get_product(product_id):
    """Retrieves a specific product by ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
        return cursor.fetchone()

def get_all_products():
    """Retrieves a list of all products from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        return cursor.fetchall()

def update_product(product_id, name, description, price, stock, provider_id):
    """Updates an existing product's details."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Products SET name = ?, description = ?, price = ?, stock = ?, provider_id = ? WHERE id = ?", (name, description, price, stock, provider_id, product_id))
        conn.commit()

def delete_product(product_id):
    """Deletes a product from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Products WHERE id = ?", (product_id,))
        conn.commit()

def record_sale(client_id, product_id, employee_id, date, total):
    """Creates a new sale in the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Sales (client_id, product_id, employee_id, date, total) VALUES (?, ?, ?, ?, ?)", (client_id, product_id, employee_id, date, total))
        conn.commit()

def get_sale(sale_id):
    """Retrieves a specific sale by ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Sales WHERE id = ?", (sale_id,))
        return cursor.fetchone()
    
def get_all_sales():
    """Retrieves a list of all sales from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Sales")
        return cursor.fetchall()
    
def update_sale(sale_id, client_id, product_id, employee_id, date, total):
    """Updates an existing sale's details."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Sales SET client_id = ?, product_id = ?, employee_id = ?, date = ?, total = ? WHERE id = ?", (client_id, product_id, employee_id, date, total, sale_id))
        conn.commit()

def delete_sale(sale_id):
    """Deletes a sale from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Sales WHERE id = ?", (sale_id,))
        conn.commit()

<<<<<<< HEAD
def record_purchase(provider_id, product_id, date, total):
=======
def create_purchase(provider_id, product_id, date, total):
>>>>>>> 5b2523ad5f8fdc432fbe2a1f3f4e1f9b4583fe93
    """Creates a new purchase in the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Purchases (provider_id, product_id, date, total) VALUES (?, ?, ?, ?)", (provider_id, product_id, date, total))
        conn.commit()

def get_purchase(purchase_id):
    """Retrieves a specific purchase by ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Purchases WHERE id = ?", (purchase_id,))
        return cursor.fetchone()
    
def get_all_purchases():
    """Retrieves a list of all purchases from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Purchases")
        return cursor.fetchall()
    
def update_purchase(purchase_id, provider_id, product_id, date, total):
    """Updates an existing purchase's details."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Purchases SET provider_id = ?, product_id = ?, date = ?, total = ? WHERE id = ?", (provider_id, product_id, date, total, purchase_id))
        conn.commit()

def delete_purchase(purchase_id):
    """Deletes a purchase from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Purchases WHERE id = ?", (purchase_id,))
        conn.commit()


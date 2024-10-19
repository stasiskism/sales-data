import psycopg2
import pandas as pd

def database_connection():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "postgres",
            user = "postgres",
            password = "postgres"
        )

        print("Database connection successful!")
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None
    
def create_tables(conn):
    cursor = conn.cursor()

    # Drop existing tables
    cursor.execute("DROP TABLE IF EXISTS products CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS stores CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS time CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS sales_transactions CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS FactSalesTransactions CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS FactSalesByProduct CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS FactSalesByStore CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS FactSalesByDate CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS FactSalesByMonth CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS FactSalesByYear CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS FactSalesByCategory CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS FactSalesByDayOfWeek CASCADE;")
    
    # Create tables
    cursor.execute("""
    CREATE TABLE products (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(255) UNIQUE,
        category VARCHAR(100),
        price DECIMAL
    );
    """
    )
    
    cursor.execute("""
    CREATE TABLE stores (
        store_id SERIAL PRIMARY KEY,
        store_name VARCHAR(255) UNIQUE,
        location VARCHAR(255),
        city VARCHAR(100),
        state VARCHAR(100)
    );
    """
    )

    cursor.execute("""
    CREATE TABLE time (
        date_id SERIAL PRIMARY KEY,
        sale_date DATE UNIQUE,
        day INT,
        month INT,
        year INT
    );
    """
    )

    cursor.execute("""
    CREATE TABLE sales_transactions (
        transaction_id SERIAL PRIMARY KEY,
        product_id INT REFERENCES products(product_id),
        store_id INT REFERENCES stores(store_id),
        quantity_sold INT,
        sale_date DATE,
        revenue DECIMAL
    );
    """
    )

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FactSalesTransactions (
            transaction_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES products(product_id),
            store_id INT REFERENCES stores(store_id),
            quantity_sold INT,
            sale_date DATE,
            total_revenue DECIMAL
        );
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FactSalesByProduct (
            product_id INT REFERENCES products(product_id),
            total_quantity_sold INT,
            total_revenue DECIMAL,
            report_date DATE,
            PRIMARY KEY (product_id, report_date)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FactSalesByStore (
            store_name varchar(200) REFERENCES stores(store_name),
            total_quantity_sold INT,
            total_revenue DECIMAL,
            report_date DATE,
            PRIMARY KEY (store_name, report_date)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FactSalesByDate (
            sale_date DATE PRIMARY KEY,
            total_quantity_sold INT,
            total_revenue DECIMAL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FactSalesByMonth (
            month VARCHAR(7) PRIMARY KEY,
            total_quantity_sold INT,
            total_revenue DECIMAL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FactSalesByYear (
            year INT PRIMARY KEY,
            total_quantity_sold INT,
            total_revenue DECIMAL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FactSalesByCategory (
            category VARCHAR(100) PRIMARY KEY,
            total_quantity_sold INT,
            total_revenue DECIMAL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FactSalesByDayOfWeek (
            day_of_week VARCHAR(10) PRIMARY KEY,
            total_quantity_sold INT,
            total_revenue DECIMAL
        );
    """)

    print("Tables created successfully!")
    cursor.close()

def insert_dim_data(data, conn):
    cursor = conn.cursor()
    products_query = """
            INSERT INTO products (product_name, category, price)
            VALUES (%s, %s, %s)
            ON CONFLICT (product_name) 
            DO NOTHING;
        """
    stores_query = """
            INSERT INTO stores (store_name, location, city)
            VALUES (%s, %s, %s)
            ON CONFLICT (store_name) 
            DO NOTHING;
        """
    time_query = """INSERT INTO time (sale_date, day, month, year) VALUES (%s, %s, %s, %s) ON CONFLICT (sale_date) DO NOTHING;"""

    for _, row in data.iterrows():
        
        cursor.execute(products_query, (row['product_name'], row['category'], row['price']))
        cursor.execute(stores_query, (row['store_name'], row['location'], row['city']))
        cursor.execute(time_query, (row['sale_date'].date(), row['day'], row['month'], row['year']))
    conn.commit()
    cursor.close()


def insert_fact_data(sales_by_product, sales_by_store, sales_by_day, sales_by_month, sales_by_year, sales_by_category, sales_by_day_of_week, conn):
    cursor = conn.cursor()

    # Insert into FactSalesTransactions
    for index, row in sales_by_day.iterrows():
        cursor.execute("""
            INSERT INTO FactSalesTransactions (store_id, product_id, quantity_sold, sale_date, total_revenue)
            VALUES (%s, %s, %s, %s, %s);
        """, (None, None, row['Total Quantity Sold'], row['Sale Date'], row['Total Revenue']))
    
    # Insert into FactSalesByProduct
    for index, row in sales_by_product.iterrows():
        cursor.execute("""
            INSERT INTO FactSalesByProduct (product_id, total_quantity_sold, total_revenue, report_date)
            VALUES ((SELECT product_id FROM products WHERE product_name = %s), %s, %s, CURRENT_DATE);
        """, (row['Product Name'], row['Total Quantity Sold'], row['Total Revenue']))
    
    # Insert into FactSalesByStore
    for index, row in sales_by_store.iterrows():
        cursor.execute("""
            INSERT INTO FactSalesByStore (store_name, total_quantity_sold, total_revenue, report_date)
            VALUES (%s, %s, %s, CURRENT_DATE);
        """, (row['Store Name'], row['Total Quantity Sold'], row['Total Revenue']))

    # Insert into FactSalesByDate
    for index, row in sales_by_day.iterrows():
        cursor.execute("""
            INSERT INTO FactSalesByDate (sale_date, total_quantity_sold, total_revenue)
            VALUES (%s, %s, %s);
        """, (row['Sale Date'], row['Total Quantity Sold'], row['Total Revenue']))

    # Insert into FactSalesByMonth
    for index, row in sales_by_month.iterrows():
        cursor.execute("""
            INSERT INTO FactSalesByMonth (month, total_quantity_sold, total_revenue)
            VALUES (%s, %s, %s);
        """, (str(row['Sale Month']), row['Total Quantity Sold'], row['Total Revenue']))

    # Insert into FactSalesByYear
    for index, row in sales_by_year.iterrows():
        cursor.execute("""
            INSERT INTO FactSalesByYear (year, total_quantity_sold, total_revenue)
            VALUES (%s, %s, %s);
        """, (int(row['Sale Year'].year), row['Total Quantity Sold'], row['Total Revenue']))

    # Insert into FactSalesByCategory
    for index, row in sales_by_category.iterrows():
        cursor.execute("""
            INSERT INTO FactSalesByCategory (category, total_quantity_sold, total_revenue)
            VALUES (%s, %s, %s);
        """, (row['Category'], row['Total Quantity Sold'], row['Total Revenue']))

    # Insert into FactSalesByDayOfWeek
    for index, row in sales_by_day_of_week.iterrows():
        cursor.execute("""
            INSERT INTO FactSalesByDayOfWeek (day_of_week, total_quantity_sold, total_revenue)
            VALUES (%s, %s, %s);
        """, (row['Day of Week'], row['Total Quantity Sold'], row['Total Revenue']))

    # Commit the transaction
    conn.commit()
    
    cursor.close()
    print("Aggregated data inserted into fact tables successfully!\n")


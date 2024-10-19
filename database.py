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
    drop_products_table = "DROP TABLE IF EXISTS products CASCADE;"
    drop_stores_table = "DROP TABLE IF EXISTS stores CASCADE;"
    drop_time_table = "DROP TABLE IF EXISTS time CASCADE;"
    drop_sales_transactions_table = "DROP TABLE IF EXISTS sales_transactions CASCADE;"

    create_products_table = """
    CREATE TABLE products (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(255),
        category VARCHAR(100),
        price DECIMAL
    );
    """
    
    create_stores_table = """
    CREATE TABLE stores (
        store_id SERIAL PRIMARY KEY,
        store_name VARCHAR(255),
        location VARCHAR(255),
        city VARCHAR(100),
        state VARCHAR(100)
    );
    """

    create_time_table = """
    CREATE TABLE time (
        date_id SERIAL PRIMARY KEY,
        day INT,
        month INT,
        year INT
    );
    """

    create_sales_transactions_table = """
    CREATE TABLE sales_transactions (
        transaction_id SERIAL PRIMARY KEY,
        product_id INT REFERENCES products(product_id),
        store_id INT REFERENCES stores(store_id),
        quantity_sold INT,
        sale_date DATE,
        revenue DECIMAL
    );
    """

    cursor.execute(drop_products_table)
    cursor.execute(drop_stores_table)
    cursor.execute(drop_time_table)
    cursor.execute(drop_sales_transactions_table)
    cursor.execute(create_products_table)
    cursor.execute(create_stores_table)
    cursor.execute(create_time_table)
    cursor.execute(create_sales_transactions_table)
    print("Tables replaced successfully!")
    cursor.close()

def read_data():
    sales_data = pd.read_csv('sales_data.csv')
    return sales_data

def insert_data(data, conn):
    cursor = conn.cursor()
    products_query = """INSERT INTO products (product_name, category, price) VALUES (%s, %s, %s)"""
    stores_query = """INSERT INTO stores (store_name, location, city) VALUES (%s, %s, %s)"""
    time_query = """INSERT INTO time (day, month, year) VALUES (%s, %s, %s)"""

    for index, row in data.iterrows():
        
        cursor.execute(products_query, (row['product_name'], row['category'], row['price']))
        cursor.execute(stores_query, (row['store_name'], row['location'], row['city']))
        sale_date = row['sale_date']
        date = pd.to_datetime(sale_date, dayfirst=True)
        cursor.execute(time_query, (date.day, date.month, date.year))
    conn.commit()
    cursor.close()


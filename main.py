from database import database_connection, create_tables, insert_dim_data, insert_fact_data
from data import read_and_clean_data, data_aggregation

conn = database_connection()
create_tables(conn)
data = read_and_clean_data()
insert_dim_data(data, conn)
sales_by_product, sales_by_store, sales_by_day, sales_by_month, sales_by_year, sales_by_category, sales_by_day_of_week = data_aggregation(data)
insert_fact_data(sales_by_product, sales_by_store, sales_by_day, sales_by_month, sales_by_year, sales_by_category, sales_by_day_of_week, conn)
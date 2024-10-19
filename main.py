from database import database_connection, create_tables, read_and_clean_data, insert_dim_data, data_aggregation

conn = database_connection()
create_tables(conn)
data = read_and_clean_data()
insert_dim_data(data, conn)
data_aggregation(data)
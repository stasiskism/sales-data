from database import database_connection, create_tables, read_data, insert_data

conn = database_connection()
create_tables(conn)
data = read_data()
insert_data(data, conn)
import pandas as pd

def read_and_clean_data():
    sales_data = pd.read_csv('sales_data.csv')

    sales_data.dropna(inplace=True)
    
    sales_data.drop_duplicates(inplace=True)

    sales_data['sale_date'] = pd.to_datetime(sales_data['sale_date'], format='%d/%m/%Y', errors='coerce')
    
    sales_data['day'] = sales_data['sale_date'].dt.day
    sales_data['month'] = sales_data['sale_date'].dt.month
    sales_data['year'] = sales_data['sale_date'].dt.year
    
    return sales_data

def data_aggregation(data):

    # Calculate total revenue for each transaction
    data['total_revenue'] = data['quantity_sold'] * data['price']
    total_revenue = data['total_revenue'].sum()
    
    print("Total Revenue: {:.2f}\n".format(total_revenue))
    
    # Sales by product
    sales_by_product = data.groupby('product_name').agg({'quantity_sold': 'sum', 'total_revenue': 'sum'}).reset_index()
    sales_by_product.columns = ['Product Name', 'Total Quantity Sold', 'Total Revenue']
    print("Sales by Product:")
    print(sales_by_product.sort_values(by='Total Revenue', ascending=False), end="\n\n")
    
    # Sales by store
    sales_by_store = data.groupby('store_name').agg({'quantity_sold': 'sum', 'total_revenue': 'sum'}).reset_index()
    sales_by_store.columns = ['Store Name', 'Total Quantity Sold', 'Total Revenue']
    print("Sales by Store:")
    print(sales_by_store.sort_values(by='Total Revenue', ascending=False), end="\n\n")
    
    # Sales by day
    data['sale_date'] = pd.to_datetime(data['sale_date'])
    sales_by_day = data.groupby(data['sale_date'].dt.date).agg({'quantity_sold': 'sum', 'total_revenue': 'sum'}).reset_index()
    sales_by_day.columns = ['Sale Date', 'Total Quantity Sold', 'Total Revenue']
    print("Sales by Day:")
    print(sales_by_day.sort_values(by='Sale Date'), end="\n\n")

    # Sales by month
    sales_by_month = data.groupby(data['sale_date'].dt.to_period('M')).agg({'quantity_sold': 'sum', 'total_revenue': 'sum'}).reset_index()
    sales_by_month.columns = ['Sale Month', 'Total Quantity Sold', 'Total Revenue']
    print("Sales by Month:")
    print(sales_by_month.sort_values(by='Sale Month'), end="\n\n")

    # Sales by year
    sales_by_year = data.groupby(data['sale_date'].dt.to_period('Y')).agg({'quantity_sold': 'sum', 'total_revenue': 'sum'}).reset_index()
    sales_by_year.columns = ['Sale Year', 'Total Quantity Sold', 'Total Revenue']
    print("Sales by Year:")
    print(sales_by_year.sort_values(by='Sale Year'), end="\n\n")

    # Average price
    average_price = data['price'].mean()
    print(f"Average Price: {average_price:.2f}\n")

    # Sales by category
    sales_by_category = data.groupby('category').agg({'quantity_sold': 'sum', 'total_revenue': 'sum'}).reset_index()
    sales_by_category.columns = ['Category', 'Total Quantity Sold', 'Total Revenue']
    print("Sales by Category:")
    print(sales_by_category.sort_values(by='Total Revenue', ascending=False), end="\n\n")

    # Sales count by category
    sales_count_by_category = data.groupby('category').size().reset_index(name='Sales Count')
    print("Sales Count by Category:")
    print(sales_count_by_category.sort_values(by='Sales Count', ascending=False), end="\n\n")

    # Percentage by category
    percentage_by_category = sales_by_category.copy()
    percentage_by_category['Percentage'] = (percentage_by_category['Total Revenue'] / total_revenue) * 100
    print("Percentage of Revenue by Category:")
    print(percentage_by_category[['Category', 'Percentage']], end="\n\n")

    # Sales by day of the week
    data['day_of_week'] = data['sale_date'].dt.day_name()
    sales_by_day_of_week = data.groupby('day_of_week').agg({'quantity_sold': 'sum', 'total_revenue': 'sum'}).reset_index()
    sales_by_day_of_week.columns = ['Day of Week', 'Total Quantity Sold', 'Total Revenue']
    print("Sales by Day of Week:")
    print(sales_by_day_of_week.sort_values(by='Total Quantity Sold', ascending=False), end="\n\n")

    return sales_by_product, sales_by_store, sales_by_day, sales_by_month, sales_by_year, sales_by_category, sales_by_day_of_week

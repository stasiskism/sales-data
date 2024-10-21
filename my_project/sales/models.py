from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.product_name
    
class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = 'stores'

    def __str__(self):
        return self.store_name
    
class Time(models.Model):
    date_id = models.AutoField(primary_key=True)
    sale_date = models.DateField(unique=True)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        db_table = 'time'

    def __str__(self):
        return str(self.sale_date)

class SalesTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    sale_date = models.DateField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'sales_transactions'

    def __str__(self):
        return f"Transaction {self.transaction_id}"


class FactSalesTransactions(models.Model):
    transaction = models.ForeignKey(SalesTransaction, on_delete=models.CASCADE)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'factsalestransactions'

    def __str__(self):
        return f"Transaction {self.transaction_id}"


class FactSalesByProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id', primary_key=True)
    total_quantity_sold = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    report_date = models.DateField()

    class Meta:
        unique_together = ('product', 'report_date')
        db_table = 'factsalesbyproduct'

    def __str__(self):
        return f"Sales by Product {self.product}"


class FactSalesByStore(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, db_column='store_name', primary_key=True)
    total_quantity_sold = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    report_date = models.DateField()

    class Meta:
        unique_together = ('store', 'report_date')
        db_table = 'factsalesbystore'

    def __str__(self):
        return f"Sales by Store {self.store}"


class FactSalesByDate(models.Model):
    sale_date = models.DateField(primary_key=True)
    total_quantity_sold = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'factsalesbydate'

    def __str__(self):
        return str(self.sale_date)


class FactSalesByMonth(models.Model):
    month = models.CharField(max_length=7, primary_key=True)
    total_quantity_sold = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'factsalesbymonth'

    def __str__(self):
        return self.month


class FactSalesByYear(models.Model):
    year = models.IntegerField(primary_key=True)
    total_quantity_sold = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'factsalesbyyear'

    def __str__(self):
        return str(self.year)


class FactSalesByCategory(models.Model):
    category = models.CharField(max_length=100, primary_key=True)
    total_quantity_sold = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'factsalesbycategory'

    def __str__(self):
        return self.category


class FactSalesByDayOfWeek(models.Model):
    day_of_week = models.CharField(max_length=10, primary_key=True)
    total_quantity_sold = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'factsalesbydayofweek'

    def __str__(self):
        return self.day_of_week
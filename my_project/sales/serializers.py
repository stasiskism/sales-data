from rest_framework import serializers
from .models import Product, Store, Time, SalesTransaction, FactSalesTransactions, FactSalesByProduct, FactSalesByStore, FactSalesByDate, FactSalesByMonth, FactSalesByYear, FactSalesByCategory, FactSalesByDayOfWeek

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'

class SalesTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTransaction
        fields = '__all__'

class FactSalesTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactSalesTransactions
        fields = '__all__'

class FactSalesByProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactSalesByProduct
        fields = '__all__'

class FactSalesByStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactSalesByStore
        fields = '__all__'

class FactSalesByDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactSalesByDate
        fields = '__all__'

class FactSalesByMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactSalesByMonth
        fields = '__all__'

class FactSalesByYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactSalesByYear
        fields = '__all__'

class FactSalesByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FactSalesByCategory
        fields = '__all__'

class FactSalesByDayOfWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactSalesByDayOfWeek
        fields = '__all__'
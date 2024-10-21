from rest_framework import generics
from .models import Product, Store, Time, SalesTransaction, FactSalesTransactions, FactSalesByProduct, FactSalesByStore, FactSalesByDate, FactSalesByMonth, FactSalesByYear, FactSalesByCategory, FactSalesByDayOfWeek
from .serializers import ProductSerializer, StoreSerializer, TimeSerializer, SalesTransactionSerializer, FactSalesTransactionsSerializer, FactSalesByProductSerializer, FactSalesByStoreSerializer, FactSalesByDateSerializer, FactSalesByMonthSerializer, FactSalesByYearSerializer, FactSalesByCategorySerializer, FactSalesByDayOfWeekSerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StoreListCreate(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class TimeListCreate(generics.ListCreateAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

class TimeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

class SalesTransactionListCreate(generics.ListCreateAPIView):
    queryset = SalesTransaction.objects.all()
    serializer_class = SalesTransactionSerializer

class SalesTransactionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesTransaction.objects.all()
    serializer_class = SalesTransactionSerializer

class FactSalesTransactionsListCreate(generics.ListCreateAPIView):
    queryset = FactSalesTransactions.objects.all()
    serializer_class = FactSalesTransactionsSerializer

class FactSalesTransactionsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactSalesTransactions.objects.all()
    serializer_class = FactSalesTransactionsSerializer

class FactSalesByProductListCreate(generics.ListCreateAPIView):
    queryset = FactSalesByProduct.objects.all()
    serializer_class = FactSalesByProductSerializer

class FactSalesByProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactSalesByProduct.objects.all()
    serializer_class = FactSalesByProductSerializer

class FactSalesByStoreListCreate(generics.ListCreateAPIView):
    queryset = FactSalesByStore.objects.all()
    serializer_class = FactSalesByStoreSerializer

class FactSalesByStoreRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactSalesByStore.objects.all()
    serializer_class = FactSalesByStoreSerializer

class FactSalesByDateListCreate(generics.ListCreateAPIView):
    queryset = FactSalesByDate.objects.all()
    serializer_class = FactSalesByDateSerializer

class FactSalesByDateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactSalesByDate.objects.all()
    serializer_class = FactSalesByDateSerializer

class FactSalesByMonthListCreate(generics.ListCreateAPIView):
    queryset = FactSalesByMonth.objects.all()
    serializer_class = FactSalesByMonthSerializer

class FactSalesByMonthRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactSalesByMonth.objects.all()
    serializer_class = FactSalesByMonthSerializer

class FactSalesByYearListCreate(generics.ListCreateAPIView):
    queryset = FactSalesByYear.objects.all()
    serializer_class = FactSalesByYearSerializer

class FactSalesByYearRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactSalesByYear.objects.all()
    serializer_class = FactSalesByYearSerializer

class FactSalesByCategoryListCreate(generics.ListCreateAPIView):
    queryset = FactSalesByCategory.objects.all()
    serializer_class = FactSalesByCategorySerializer

class FactSalesByCategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactSalesByCategory.objects.all()
    serializer_class = FactSalesByCategorySerializer

class FactSalesByDayOfWeekListCreate(generics.ListCreateAPIView):
    queryset = FactSalesByDayOfWeek.objects.all()
    serializer_class = FactSalesByDayOfWeekSerializer

class FactSalesByDayOfWeekRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactSalesByDayOfWeek.objects.all()
    serializer_class = FactSalesByDayOfWeekSerializer
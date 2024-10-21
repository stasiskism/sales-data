from django.urls import path
from .views import ProductListCreate, ProductRetrieveUpdateDestroy, StoreListCreate, StoreRetrieveUpdateDestroy, TimeListCreate, TimeRetrieveUpdateDestroy, SalesTransactionListCreate, SalesTransactionRetrieveUpdateDestroy, FactSalesTransactionsListCreate, FactSalesTransactionsRetrieveUpdateDestroy, FactSalesByProductListCreate, FactSalesByProductRetrieveUpdateDestroy, FactSalesByStoreListCreate, FactSalesByStoreRetrieveUpdateDestroy, FactSalesByDateListCreate, FactSalesByDateRetrieveUpdateDestroy, FactSalesByMonthListCreate, FactSalesByMonthRetrieveUpdateDestroy, FactSalesByYearListCreate, FactSalesByYearRetrieveUpdateDestroy, FactSalesByCategoryListCreate, FactSalesByCategoryRetrieveUpdateDestroy, FactSalesByDayOfWeekListCreate, FactSalesByDayOfWeekRetrieveUpdateDestroy

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name = 'item-retrieve-update-destroy'),
    path('stores/', StoreListCreate.as_view(), name='store-list-create'),
    path('stores/<int:pk>/', StoreRetrieveUpdateDestroy.as_view(), name='store-detail'),
    path('time/', TimeListCreate.as_view(), name='time-list-create'),
    path('time/<int:pk>/', TimeRetrieveUpdateDestroy.as_view(), name='time-detail'),
    path('sales-transactions/', SalesTransactionListCreate.as_view(), name='sales-transaction-list-create'),
    path('sales-transactions/<int:pk>/', SalesTransactionRetrieveUpdateDestroy.as_view(), name='sales-transaction-detail'),
    path('fact-sales-transactions/', FactSalesTransactionsListCreate.as_view(), name='fact-sales-transactions-list-create'),
    path('fact-sales-transactions/<int:pk>/', FactSalesTransactionsRetrieveUpdateDestroy.as_view(), name='fact-sales-transactions-detail'),
    path('fact-sales-by-product/', FactSalesByProductListCreate.as_view(), name='fact-sales-by-product-list-create'),
    path('fact-sales-by-product/<int:pk>/', FactSalesByProductRetrieveUpdateDestroy.as_view(), name='fact-sales-by-product-detail'),
    path('fact-sales-by-store/', FactSalesByStoreListCreate.as_view(), name='fact-sales-by-store-list-create'),
    path('fact-sales-by-store/<int:pk>/', FactSalesByStoreRetrieveUpdateDestroy.as_view(), name='fact-sales-by-store-detail'),
    path('fact-sales-by-date/', FactSalesByDateListCreate.as_view(), name='fact-sales-by-date-list-create'),
    path('fact-sales-by-date/<int:pk>/', FactSalesByDateRetrieveUpdateDestroy.as_view(), name='fact-sales-by-date-detail'),
    path('fact-sales-by-month/', FactSalesByMonthListCreate.as_view(), name='fact-sales-by-month-list-create'),
    path('fact-sales-by-month/<int:pk>/', FactSalesByMonthRetrieveUpdateDestroy.as_view(), name='fact-sales-by-month-detail'),
    path('fact-sales-by-year/', FactSalesByYearListCreate.as_view(), name='fact-sales-by-year-list-create'),
    path('fact-sales-by-year/<int:pk>/', FactSalesByYearRetrieveUpdateDestroy.as_view(), name='fact-sales-by-year-detail'),
    path('fact-sales-by-category/', FactSalesByCategoryListCreate.as_view(), name='fact-sales-by-category-list-create'),
    path('fact-sales-by-category/<int:pk>/', FactSalesByCategoryRetrieveUpdateDestroy.as_view(), name='fact-sales-by-category-detail'),
    path('fact-sales-by-day-of-week/', FactSalesByDayOfWeekListCreate.as_view(), name='fact-sales-by-day-of-week-list-create'),
    path('fact-sales-by-day-of-week/<int:pk>/', FactSalesByDayOfWeekRetrieveUpdateDestroy.as_view(), name='fact-sales-by-day-of-week-detail')
]
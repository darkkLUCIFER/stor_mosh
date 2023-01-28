from django.urls import path
from store.api.views import product_detail, collection_list, collection_detail, ProductList

app_name = 'api'

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('collections/', collection_list, name='collection-list'),
    path('collections/<int:pk>/', collection_detail, name='collection-detail'),
]

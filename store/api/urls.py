from django.urls import path
from store.api.views import product_list, product_detail, collection_list, collection_detail

app_name = 'api'

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('collections/', collection_list, name='collection-list'),
    path('collections/<int:pk>/', collection_detail, name='collection-detail'),
]

from django.urls import path
from store.api.views import ProductDetail, CollectionList, CollectionDetail, ProductList

app_name = 'api'

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('collections/', CollectionList.as_view(), name='collection-list'),
    path('collections/<int:pk>/', CollectionDetail.as_view(), name='collection-detail'),
]

from django.urls import path, include

app_name = 'store'

urlpatterns = [
    path('store/', include('store.api.urls', namespace='store-api')),
]

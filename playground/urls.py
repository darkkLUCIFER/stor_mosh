from django.urls import path
from playground.views import hello
app_name = 'playground'

urlpatterns = [
    path('hello/', hello, name='hello'),
]

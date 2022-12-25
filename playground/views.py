from django.shortcuts import render
from django.db.models import Count, Min, Max
from django.db.models import Value, F
from store.models import Product, Order


def hello(request):
    query_set = Product.objects.annotate(is_new=F('id'))
    return render(request, 'playground/hello.html', {'products': query_set})

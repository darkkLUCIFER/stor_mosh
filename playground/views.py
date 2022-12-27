from django.shortcuts import render
from django.db.models import Count, Min, Max
from django.db.models import Value, F
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Order, Collection, OrderItem
from tags.models import TaggedItem


def hello(request):
    queryset = Product.objects.raw('SELECT * FROM store_product')

    return render(request, 'playground/hello.html', {'result': list(queryset)})

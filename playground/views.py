from django.shortcuts import render
from django.db.models import Count, Min, Max
from django.db.models import Value, F
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Order, Collection, OrderItem
from tags.models import TaggedItem


# @transaction.atomic()
def hello(request):
    with transaction.atomic():
        order = Order.objects.create(customer_id=1)

        item = OrderItem.objects.create(order=order, product_id=1, quantity=1, unit_price=10)
    return render(request, 'playground/hello.html', {})

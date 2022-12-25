from django.shortcuts import render
from django.db.models import Count, Min, Max
from django.db.models import Value, F
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Order
from tags.models import TaggedItem


def hello(request):
    tags = TaggedItem.objects.get_tags_for(Product, 1)
    return render(request, 'playground/hello.html', {'tags': list(tags)})

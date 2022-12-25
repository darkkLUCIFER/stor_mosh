from django.shortcuts import render
from django.db.models import Count, Min, Max
from django.db.models import Value, F
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Order
from tags.models import TaggedItem


def hello(request):
    content_type = ContentType.objects.get_for_model(Product)

    query_set = TaggedItem.objects.select_related('tag').filter(
        content_type=content_type,
        object_id=1
    )
    return render(request, 'playground/hello.html', {'tags': list(query_set)})

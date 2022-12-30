from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse

from store.models import Customer, Collection, Product, Order


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_product', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
                reverse('admin:store_product_changelist')
                + '?'
                + urlencode({
            'collection__id': str(collection.id)
        }))
        return format_html('<a href="{}">{}</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'

    @admin.action(description='clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.'

        )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'customer']

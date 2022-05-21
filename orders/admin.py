from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'order_date', 'order_heading', 'order_signed_doc')
    list_filter = ('order_date',)
    search_fields = ['order_number', 'order_heading']


admin.site.register(Order, OrderAdmin)



from django.contrib import admin
from django.conf import settings

from .models import Orders


class OrderAdmin(admin.ModelAdmin):
    model = Orders
    list_display = ('jmeno', 'prijmeni', 'email')


admin.site.register(Orders, OrderAdmin)

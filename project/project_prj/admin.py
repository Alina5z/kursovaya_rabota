from django.contrib import admin
from .models import Task, Orders


@admin.register(Task)
class StatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manufacturer', 'price', 'square')
    list_display_links = ('id', 'name', 'manufacturer', 'price', 'square')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'owner', 'task')
    list_display_links = ('id', 'created', 'owner', 'task')

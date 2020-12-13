from django.contrib import admin
from .models import Category, Item, Price
# Register your models here.

admin.site.register(Category)
# admin.site.register(Item)
admin.site.register(Price)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'available_units', 'display_price', 'display_category')


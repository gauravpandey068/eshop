from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_filter = ['category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']



class AdminCustomer(admin.ModelAdmin):
    list_display=['email']


class AdminOrder(admin.ModelAdmin):
    list_display = ['product','price','done','address']
    list_filter = ['done']


admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Customer, AdminCustomer )
admin.site.register(Order, AdminOrder )

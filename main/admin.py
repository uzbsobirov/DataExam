from django.contrib import admin
from .models import Category, Product, Inventory, ProductPhoto, Customer, Order


uneditable_fields = ('id', 'date_created', 'date_updated')

# admin.site.register(Order)
# admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(ProductPhoto)
admin.site.register(Customer)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'description'
    )

    fields = [field.name for field in Category._meta.fields if field.name not in uneditable_fields]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'description',
        'price'
    )
    
    fields = [field.name for field in Product._meta.fields if field.name not in uneditable_fields]
    prepopulated_fields = {'slug': ('name',)}

# @admin.register(Inventory)
# class InventoryAdmin(admin.ModelAdmin):
#     list_display = (
#         'product',
#         'stock_status',
#         'quantity'
#     )
    
#     fields = [field.name for field in Inventory._meta.fields if field.name not in uneditable_fields]

# @admin.register(ProductPhoto)
# class ProductPhotoAdmin(admin.ModelAdmin):
#     list_display = (
#         'product',
#         'thumbnail_pc',
#         'large_pc'
#     )
    
#     fields = [field.name for field in ProductPhoto._meta.fields if field.name not in uneditable_fields]

# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = (
#         'full_name',
#         'email',
#         'phone_number',
#         'address'
#     )
    
#     fields = [field.name for field in Customer._meta.fields if field.name not in uneditable_fields]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
    )
    
    fields = [field.name for field in Order._meta.fields if field.name not in uneditable_fields]


from django.contrib import admin
from .models import Category, Product, SubCategory

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget



# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


# @admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(SubCategory, SubCategoryAdmin)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'price',
#                     'available', 'created', 'updated', 'category']
#     list_filter = ['available', 'created', 'updated']
#     list_editable = ['price', 'available']
#     prepopulated_fields = {'slug': ('name',)}


class ProductResource(resources.ModelResource):
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name')
    )

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'image', 'characteristics', 'description', 'price', 'available', 'created', 'updated')
        export_order = ('id', 'category', 'name', 'image', 'characteristics', 'description', 'price', 'available', 'created', 'updated')

class ProductAdmin(ImportExportActionModelAdmin):
    resource_class = ProductResource
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated', 'category']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
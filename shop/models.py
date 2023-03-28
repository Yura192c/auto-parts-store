from django.db import models
from django.urls import reverse

# Create your models here.
# TODO продумать структуру хранения характеристик товара
# TODO продумать модели в бд и их связи(создать модели)

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to=f'SubCategory/{slug}', blank=True, null=True)
    # products = models.ManyToManyField(Product, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_subcategory', args=[self.category.slug, self.slug])


class Product(models.Model):
    category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    characteristics = models.JSONField(blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=10)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.category.category.slug, self.category.slug ,self.id, self.slug])




# class Car(models.Model):
#     # vin_code = models.CharField(max_length=17, help_text="VIN код машины")
#     make = models.CharField(max_length=255, help_text="Марка машины")
#     model = models.CharField(max_length=255, help_text="Модель машины")
#     year = models.IntegerField(help_text="Год выпуска машины")
#     # products = models.ManyToManyField(Product)
#     engine_type = models.CharField(max_length=255, help_text="Тип двигателя")
    
#     class Meta:
#         ordering = ('make',)
#         verbose_name = 'Машина'
#         verbose_name_plural = 'Машины'

#     def __str__(self):
#         return f'{self.make} {self.model} {self.year}'


# class ProductVehicle(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     # vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

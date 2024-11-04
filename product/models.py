from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 20)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_images', blank=False, null=False)

    def __str__(self):
        return self.name

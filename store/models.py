from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='URL', unique=True)
    image = models.ImageField(upload_to='categories', blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('store:category', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'



class Product(models.Model):
    AGE_CHOICES =(
        ("1", "0-12 месяцев"),
        ("2", "1-3 года"),
        ("3", "4-5 лет"),
        ("4", "6-8 лет"),
        ("5", "9-12 лет"),
        ("6", "более 12 лет"),
    )

    category = models.ManyToManyField(Category, blank=True, related_name='products')
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    manufacturer_country = models.CharField(max_length=50)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT,  blank=True, null=True)
    article = models.CharField(max_length=50)
    package_size = models.CharField(max_length=100, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('store:product', kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)


class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name='Бренд')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)

    def get_absolute_url(self):
        return reverse('store:brand', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'



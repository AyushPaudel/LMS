from django.db import models
from django.conf import settings


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url_slug = models.SlugField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return (str(self.title))


class SubCategories(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url_slug = models.SlugField(unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return (str(self.title))


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    url_slug = models.SlugField(unique=True)
    sub_categories_id = models.ForeignKey(
        SubCategories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    original_stock = models.PositiveIntegerField(default=1)
    total_stock = models.PositiveIntegerField(default=1)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return str(self.product_name)


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    product_taken = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_taken')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_id')
    lab_incharge = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="incharge_id")












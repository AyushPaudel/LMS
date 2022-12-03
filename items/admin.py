from django.contrib import admin

from models import Products, Categories, SubCategories, Transaction
# Register your models here.


admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Transaction)
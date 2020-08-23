from django.contrib import admin
from .models import Products, Offers


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')


admin.site.register(Offers,OfferAdmin)
admin.site.register(Products,ProductAdmin)


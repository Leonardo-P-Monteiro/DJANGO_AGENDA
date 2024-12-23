from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Category)
class CategoryAdm(admin.ModelAdmin):
    list_display = 'category_name',
    ordering = '-id',

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'owner', 'show',
    ordering = '-id',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    # list_editable = 'first_name', 'last_name', 'show',
    list_editable = 'show',
    list_display_links = 'phone', 'id', 'first_name', 'last_name',
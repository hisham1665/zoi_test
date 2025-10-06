from django.contrib import admin
from .models import Category, Expense

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'category', 'date']
    list_filter = ['category', 'date']
    search_fields = ['title', 'category__name']
    date_hierarchy = 'date'

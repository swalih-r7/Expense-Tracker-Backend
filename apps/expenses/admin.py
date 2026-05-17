from django.contrib import admin
from .models import Category, Expense

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'color', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'category', 'description', 'transaction_date', 'payment_method')
    list_filter = ('category', 'payment_method', 'transaction_date', 'is_recurring')
    search_fields = ('description', 'user__email')
    raw_id_fields = ('user',)
    date_hierarchy = 'transaction_date'
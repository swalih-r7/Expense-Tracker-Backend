from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=50, blank=True, default='💰')
    color = models.CharField(max_length=20, default='#3B82F6')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Expense(models.Model):
    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('CREDIT_CARD', 'Credit Card'),
        ('DEBIT_CARD', 'Debit Card'),
        ('UPI', 'UPI'),
        ('BANK_TRANSFER', 'Bank Transfer'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='expenses')
    description = models.TextField(blank=True)
    transaction_date = models.DateTimeField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='CASH')
    receipt_image = models.ImageField(upload_to='receipts/', blank=True, null=True)
    is_recurring = models.BooleanField(default=False)
    recurring_frequency = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'expenses'
        ordering = ['-transaction_date']
        indexes = [
            models.Index(fields=['user', 'transaction_date']),
            models.Index(fields=['user', 'category']),
        ]
    
    def __str__(self):
        return f"{self.user.email} - ${self.amount} - {self.transaction_date}"
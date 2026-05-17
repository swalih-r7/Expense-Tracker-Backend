from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db.models import Sum, Avg, Max, Min, Count
from django.utils import timezone
from datetime import timedelta
from .models import Expense, Category
from .serializers import ExpenseSerializer, ExpenseCreateUpdateSerializer, CategorySerializer
from .permissions import IsOwner

class ExpenseListCreateView(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsOwner]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['description', 'category__name']
    ordering_fields = ['amount', 'transaction_date', 'created_at']
    ordering = ['-transaction_date']
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseCreateUpdateSerializer
    permission_classes = [IsOwner]
    
    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []

class DashboardSummaryView(APIView):
    def get(self, request):
        user = request.user
        expenses = Expense.objects.filter(user=user)
        today = timezone.now()
        start_of_month = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        start_of_week = today - timedelta(days=today.weekday())
        
        summary = {
            'total_expenses': expenses.aggregate(total=Sum('amount'))['total'] or 0,
            'monthly_total': expenses.filter(transaction_date__gte=start_of_month).aggregate(total=Sum('amount'))['total'] or 0,
            'weekly_total': expenses.filter(transaction_date__gte=start_of_week).aggregate(total=Sum('amount'))['total'] or 0,
            'average_expense': expenses.aggregate(avg=Avg('amount'))['avg'] or 0,
            'highest_expense': expenses.aggregate(max=Max('amount'))['max'] or 0,
            'lowest_expense': expenses.aggregate(min=Min('amount'))['min'] or 0,
            'total_transactions': expenses.count(),
        }
        return Response(summary)
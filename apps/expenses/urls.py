from django.urls import path
from .views import ExpenseListCreateView, ExpenseDetailView, CategoryListCreateView, DashboardSummaryView

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('dashboard/summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),
]
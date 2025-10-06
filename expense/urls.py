from django.urls import path
from . import views

urlpatterns = [
    path('expenses/', views.add_expenses, name='add_expenses'),
    path('expenses/summary/', views.expenses_summary, name='expenses_summary'),
    path('categories/add/', views.add_category, name='add_category'),
    path('expenses/add/', views.add_expense_form, name='add_expense_form'),
]

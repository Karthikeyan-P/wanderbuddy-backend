from django.urls import path
from expenses.views import create_expense, total_trip_expense

urlpatterns = [
    path('createExpense/<int:trip_id>/', create_expense, name='create_expense'),
    path('totalExpense/<int:trip_id>/', total_trip_expense, name='total_trip_expense'),
]

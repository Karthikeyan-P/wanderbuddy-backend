from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tripmgmt.models import Trip
from expenses.models import Expense
from expenses.serializers import ExpenseSerializer

@api_view(['POST'])
def create_expense(request, trip_id):
    """
    Create an expense for a trip and share it among all the participants.
    """
    trip = get_object_or_404(Trip, id=trip_id)

    # Check if the request data is valid
    serializer = ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        expense = serializer.save(trip=trip)

        # Share the expense equally among all participants
        participants_count = trip.participants.count()
        if participants_count > 0:
            shared_amount = expense.amount / participants_count
            for participant in trip.participants.all():
                participant.expenses_paid.add(expense)
                participant.save()

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def total_trip_expense(request, trip_id):
    """
    View the total expense of the trip.
    """
    trip = get_object_or_404(Trip, id=trip_id)
    total_expense = sum(expense.amount for expense in trip.expense_set.all())
    return Response({'total_trip_expense': total_expense})

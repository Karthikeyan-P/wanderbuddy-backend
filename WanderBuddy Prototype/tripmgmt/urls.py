from django.urls import path, include

from tripmgmt import views

urlpatterns = [
    path('trips/', views.getTrips, name='trips'),
   # path('participants/', views.getAllParticipants, name='participants'),
    path('trip/<int:trip_id>/participants/', views.getParticipants),
    path('createtrip/', views.createTrip, name='createtrip'),
    path('upcomingtrips/<int:participant_id>/', views.getUpcomingTrips)
]
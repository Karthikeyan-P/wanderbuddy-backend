from django.urls import path, include

from tripmgmt import views

urlpatterns = [
   path('trips/', views.getTrips, name='trips'),
   path('trip/<int:trip_id>/participants/', views.getParticipants),
   path('createtrip/', views.createTrip, name='createtrip'),
   path('upcomingtrips/<int:participant_id>/', views.getUpcomingTrips),
   path('participant/<int:participant_id>/', views.getParticipant),
   path('addParticipant/<int:trip_id>/', views.addParticipant),
   path('messages/<int:chatroom_id>/', views.handle_messages),
   path('createchatroom/<int:trip_id>/', views.create_chatroom)
]
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from tripmgmt.models import Trip, Participant, Image
from tripmgmt.serializers import ParticipantSerializer, TripSerializer, ImageSerializer

@api_view(['GET'])
def getParticipants(request, trip_id):
    trip = Trip.objects.get(id = trip_id)
    participants = trip.participants.all() #using reverse relationship
    serializer = ParticipantSerializer(participants, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTrips(request):
    trips = Trip.objects.all()

    for trip in trips :
        trip_dict = TripSerializer(trip).data
        organizer_data = ParticipantSerializer(trip.organizer).data
        participants_data = ParticipantSerializer(trip.participants.all(), many=True).data
        trip_dict['organizer'] = organizer_data
        trip_dict['participants'] = participants_data

    return Response(trip_dict)


@api_view(['GET'])
def getUpcomingTrips(request, participant_id):
    participant = Participant.objects.get(id = participant_id)
    trips = participant.trips.all()
    trip_data = []
    for trip in trips:
        trip_dict = TripSerializer(trip).data
        organizer_data = ParticipantSerializer(trip.organizer).data
        participants_data = ParticipantSerializer(trip.participants.all(), many=True).data
        img = Image.objects.filter(trip__id = trip.id)
        print(img)
        trip_img = ImageSerializer(img, many=True).data
        trip_dict['organizer'] = organizer_data
        trip_dict['participants'] = participants_data
        trip_dict['tripimages'] = trip_img
        trip_data.append(trip_dict)
    return Response(trip_data)
   # serializer = TripSerializer(trips, many=True)
   # return Response(serializer.data)



@api_view(['POST'])
def createTrip(request):
    serializer = TripSerializer(data = request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET'])
# def getAllParticipants(request):
#     res = Participant.objects.all()
#     serializer = ParticipantSerializer(res, many=True)
#     return Response(serializer.data)
  
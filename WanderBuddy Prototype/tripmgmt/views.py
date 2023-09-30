import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from tripmgmt.models import Chatroom, Message, Trip, Participant, Image
from tripmgmt.serializers import MsgSerializer, ParticipantSerializer, TripSerializer, ImageSerializer

# API to get participants of a trip
@api_view(['GET'])
def getParticipants(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    participants = trip.participants.all()  # using reverse relationship
    serializer = ParticipantSerializer(participants, many=True)
    return Response(serializer.data)

# API to view all trips
@api_view(['GET'])
def getTrips(request):
    trips = Trip.objects.all()
    trip_data = []
    for trip in trips:
        trip_dict = TripSerializer(trip).data
        organizer_data = ParticipantSerializer(trip.organizer).data
        participants_data = ParticipantSerializer(
            trip.participants.all(), many=True).data
        trip_dict['organizer'] = organizer_data
        trip_dict['participants'] = participants_data
        trip_data.append(trip_dict)
    return Response(trip_data)


# API to view upcoming trips for a logged in user.
@api_view(['GET'])
def getUpcomingTrips(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    trips = participant.trips.all()
    trip_data = []
    for trip in trips:
        trip_dict = TripSerializer(trip).data
        organizer_data = ParticipantSerializer(trip.organizer).data
        participants_data = ParticipantSerializer(
            trip.participants.all(), many=True).data
        img = Image.objects.filter(trip__id=trip.id)
        trip_img = ImageSerializer(img, many=True).data
        trip_dict['organizer'] = organizer_data
        trip_dict['participants'] = participants_data
        trip_dict['tripimages'] = trip_img
        trip_data.append(trip_dict)
    return Response(trip_data)

# API to create a new trip
@api_view(['POST'])
def createTrip(request):
    serializer = TripSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API to add participant to a trip. Will be used once Karthi's changes are merged
@api_view(['POST'])
def addParticipant(request, trip_id):
    participant_id = request.data.get('participant_id')
    trip = Trip.objects.get(id=trip_id)
    try:
        participant = Participant.objects.get(id=participant_id)
        trip.participants.add(participant)
        return Response('success', status=status.HTTP_201_CREATED)

    except Participant.DoesNotExist:
        return Response('Error')


# API to create a chatroom for a trip, if it does not exist already
@api_view(['GET'])
def create_chatroom(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    try:
        chatroomID = Chatroom.objects.get(trip=trip).id
    except Chatroom.DoesNotExist:
        members = trip.participants.all()
        chatroom = Chatroom.objects.create(trip=trip)
        chatroom.participants.set(members)
        chatroomID = Chatroom.objects.get(trip=trip).id
    return Response({'chatroomID': chatroomID, 'message': 'success'}, status=status.HTTP_201_CREATED)


# API to send messages
@api_view(['GET', 'POST'])
def handle_messages(request, chatroom_id):
    if request.method == 'GET':
        chatroom = Chatroom.objects.get(id=chatroom_id)
        messages = Message.objects.filter(chatroom=chatroom)
        serializer = MsgSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        content = request.data.get('content')
        sender = Participant.objects.get(id=2)
        print(sender)
        messages = Message.objects.create(
            chatroom_id=chatroom_id,
            content=content,
            sender=sender
        )
        chatroom = Chatroom.objects.get(id=chatroom_id)
        messages = Message.objects.filter(chatroom=chatroom)

        # Serialize the messages
        serializer = MsgSerializer(messages, many=True)

        return Response(serializer.data)

@api_view(['GET'])
def getParticipant(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    serializer = ParticipantSerializer(participant)
    return Response(serializer.data)



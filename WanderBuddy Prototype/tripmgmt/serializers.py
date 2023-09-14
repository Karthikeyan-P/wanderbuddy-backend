from rest_framework import serializers

from tripmgmt.models import Image, Trip, Participant

class TripSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Trip
        fields = "__all__"


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Participant
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["image"]
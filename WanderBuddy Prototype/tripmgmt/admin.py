from django.contrib import admin

from tripmgmt.models import Chatroom, Trip, Participant, Image, Message

#Register your models here.
admin.site.register(Trip)
admin.site.register(Participant)
admin.site.register(Image)
admin.site.register(Message)
admin.site.register(Chatroom)
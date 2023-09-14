from django.contrib import admin

from tripmgmt.models import Trip, Participant, Image

#Register your models here.
admin.site.register(Trip)
admin.site.register(Participant)
admin.site.register(Image)
from django.contrib import admin
from .models import Event,Event_authorized_user,Performance,Ticket,Drawing
# Register your models here.

admin.site.register(Event)
admin.site.register(Event_authorized_user)
admin.site.register(Ticket)
admin.site.register(Performance)
admin.site.register(Drawing)
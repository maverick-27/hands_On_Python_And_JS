from django.contrib import admin
from .models import RoomBelongsToDuo,Room,ChatMessage
# Register your models here.

admin.site.register(Room)
admin.site.register(ChatMessage)
admin.site.register(RoomBelongsToDuo)



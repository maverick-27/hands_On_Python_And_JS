from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.




class Room(models.Model):
    room_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    room_name = models.CharField (max_length=128, blank=True, null=True)
    def __str__(self):
        """
        String to represent the message
        """

        return str("{} - {}".format(self.room_name,self.room_id))

class RoomBelongsToDuo(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
 
        return str("{} - {}".format(self.room,self.user))



class ChatMessage(models.Model):
    """
    Model to represent a chat message
    """

    #Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_room = models.ForeignKey(Room,on_delete=models.CASCADE)
    message = models.TextField(max_length=3000)
    message_html = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String to represent the message
        """

        return self.message
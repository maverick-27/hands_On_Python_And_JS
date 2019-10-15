from rest_framework import serializers
from .models import ChatMessage
from django.contrib.auth.models import User


# class ActiveUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ActiveUser
        

# class EventSerializer(serializers.ModelSerializer):

#     event_creator= ActiveUserSerializer
#     class Meta:
#         model=Event
#         fields=['event_creator','event_status','event_level_category','end_date']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields=['username']  

class ChatMessageSerializer(serializers.ModelSerializer):

   
    class Meta:
        model = ChatMessage
        fields='__all__'
     


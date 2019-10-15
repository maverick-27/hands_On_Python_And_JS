from django.shortcuts import render
from uuid import uuid4
from rest_framework.generics import ListCreateAPIView
from .models import ChatMessage,Room,RoomBelongsToDuo,ChatMessage
from .serializers import ChatMessageSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.




class ChatCreateListView(ListCreateAPIView):


    def list(self,request):

        user = self.request.user
        print(user)
        users_belongs_to_room = RoomBelongsToDuo.objects.get(user = user)
        room_found  = Room.objects.get(room_id=users_belongs_to_room.room.room_id)


        queryset = ChatMessage.objects.filter(message_room=room_found)
        serializer = ChatMessageSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request,*args, **kwargs):
        user = self.request.user
        print("USER IS --->>>",user)


        users_belongs_to_room = RoomBelongsToDuo.objects.get(user = user)
        room_found  = Room.objects.get(room_id=users_belongs_to_room.room.room_id)

        chat_reply = request.data
        print(chat_reply)
        message=chat_reply['chat_reply']
        data = {'user':user.id,'message_room':room_found.room_id,'message':message,'message_html':message}

        serializer = ChatMessageSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    



        print("HERE......",message)



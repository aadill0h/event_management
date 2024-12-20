from django.shortcuts import render
from rest_framework import status
from .serializers import CreateEventSerializer, UpdateEventSerializer , ListEventSerializer, RegistrationSerializer
from .models import Events,Registrations
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class CreateEventView(APIView):
    serializer_class = CreateEventSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            # Use the serializer's create() method to handle event creation
            event = serializer.save()
            
            return Response(
                {"message": "Event created successfully"},
                status=status.HTTP_201_CREATED
            )
        
        # Return validation errors if any
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateEventView(APIView):
    def put(self, request, eventId, format=None):
        try:
            event = Events.objects.get(id=eventId)
        except Events.DoesNotExist:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Initialize the serializer with the event instance and request data
        serializer = UpdateEventSerializer(event, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()  # This will trigger the custom `update` method
            return Response(
                {"message": "Event updated successfully"},
                status=status.HTTP_200_OK
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListEventView(APIView):
    def get(self, request, format=None):
        events = Events.objects.all()
        serializer =ListEventSerializer(events, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class RegistrationView(APIView):
    def post(self, request, eventId, *args, **kwargs):
        try:
            event = Events.objects.get(id = eventId)
        except Events.DoesNotExist:
            return Response(
                {"error":"event not found"}, status=status
            )
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event = event)
            return Response(
                {"message":"registration successfull", "data":serializer.data},status = status.HTTP_201_CREATED
            )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
class EventDetailsView(APIView):
    def get(self, request, eventId):
        try:
            event = Events.objects.get(id=eventId)
        except Events.DoesNotExist:
            return Response({"error": "Event Not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ListEventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EventDeleteView(APIView):
    def delete(self, request , eventId):
        try:
            event = Events.objects.get(id=eventId)
            event.delete()
            return Response(
                {"message":"eventc deleted successfully"},
                status = status.HTTP_204_NO_CONTENT
            )
        except Events.DoesNotExist:
            return Response(
                {"error":"event not found"},
                status=status.HTTP_404_NOT_FOUND
            )

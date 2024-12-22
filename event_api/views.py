from django.shortcuts import render
from rest_framework import status
from .serializers import CreateEventSerializer, UpdateEventSerializer , ListEventSerializer, RegistrationSerializer,ViewEventAttendanceSerialiser,EditEventAttendanceSerializer, ViewEventFeedbackSerialiszer,EditEventFeedbackSerializer
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
                {"error":"event not found"}, status=status.HTTP_404_NOT_FOUND
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

class ViewEventAttendanceView(APIView):
    def get(self, request, eventId):
        try:
            event = Events.objects.get(id=eventId)
        except Events.DoesNotExist:
            return Response({"error":"event not found"},status = status.HTTP_404_NOT_FOUND)
        attendees = Registrations.objects.filter(event=event)
        serializer = ViewEventAttendanceSerialiser(attendees,many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
class EditEventAttendanceView(APIView):
    def get(self, request, eventId):
        try:
            event = Events.objects.get(id=eventId)
        except Events.DoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)

        registrations = Registrations.objects.filter(event=event)
        serializer = ViewEventAttendanceSerialiser(registrations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, eventId, format=None):
        try:
            event = Events.objects.get(id=eventId)
        except Events.DoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)

        registrations = Registrations.objects.filter(event=event)

        serializer = EditEventAttendanceSerializer(data=request.data, many=True, partial=True)
        if serializer.is_valid():
            for record in serializer.validated_data:
                try:
                    registration = Registrations.objects.get(event=event, studentId=record['studentId'])
                except Registrations.DoesNotExist:
                    return Response({"error": f"Registration for studentId {record['studentId']} not found"}, status=status.HTTP_404_NOT_FOUND)

                registration.attendance = record.get("attendance", registration.attendance)
                registration.save()

            return Response({"message": "Attendance updated successfully"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViewEventFeedbackView(APIView):
    def get(self , request , eventId):
        try :
            event = Events.objects.get(id = eventId)
        except Events.DoesNotExist:
            return Render(
                {"error":"event not found"},status = status.HTTP_404_NOT_FOUND
            )
        feedback  = Registrations.objects.filter(event = event)
        serializer = ViewEventFeedbackSerialiszer(feedback, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateFeedbackView(APIView):
    def put(self, request, registrationId, format=None):
        try:
            registration = Registrations.objects.get(id=registrationId)
        except Registrations.DoesNotExist:
            return Response({"error": "Registration does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if not registration.attendance:
            return Response({"error": "Feedback can only be provided if attendance is True"}, status=status.HTTP_403_FORBIDDEN)

        serializer = EditEventFeedbackSerializer(registration, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Feedback submitted successfully"}, status=status.HTTP_200_OK
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

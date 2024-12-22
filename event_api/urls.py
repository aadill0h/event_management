from django.urls import path
from .views import CreateEventView,UpdateEventView,ListEventView,RegistrationView,EventDetailsView,EventDeleteView,ViewEventAttendanceView, EditEventAttendanceView,CreateFeedbackView,ViewEventFeedbackView

urlpatterns = [
    path('events/create/',CreateEventView.as_view()),
    path('event/update/<int:eventId>/',UpdateEventView.as_view(),name = 'update-event'),
    path('events/all/',ListEventView.as_view()),
    path('events/register/<int:eventId>/',RegistrationView.as_view()),
    path('events/<int:eventId>/',EventDetailsView.as_view()),
    path('events/<int:eventId>/delete/',EventDeleteView.as_view()),
    path('events/attendance/view/<int:eventId>/',ViewEventAttendanceView.as_view()),
    path('events/attendance/edit/<int:eventId>/',EditEventAttendanceView.as_view()),
    path('events/feedback/<int:registrationId>/',CreateFeedbackView.as_view()),
    path('events/feedback/view/<int:eventId>/',ViewEventFeedbackView.as_view()),
]
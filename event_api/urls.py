from django.urls import path
from .views import CreateEventView,UpdateEventView,ListEventView,RegistrationView,EventDetailsView,EventDeleteView

urlpatterns = [
    path('events/create/',CreateEventView.as_view()),
    path('event/update/<int:eventId>/',UpdateEventView.as_view(),name = 'update-event'),
    path('events/all/',ListEventView.as_view()),
    path('events/register/<int:eventId>/',RegistrationView.as_view()),
    path('events/<int:eventId>/',EventDetailsView.as_view()),
    path('events/<int:eventId>/delete/',EventDeleteView.as_view()),
]
from rest_framework import serializers
from .models import Events,Tag, Registrations

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_name',)

class CreateEventSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)  # For response
    tag_ids = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, write_only=True)  # For input

    class Meta:
        model = Events
        fields = ('title', 'description', 'date', 'time', 'venue', 'capacity', 'organiser', 'tags', 'tag_ids')
    
    def create(self, validated_data):
        tag_ids = validated_data.pop('tag_ids')
        event = Events.objects.create(**validated_data)
        event.tags.set(tag_ids)  # Associate tags with the event
        return event

class UpdateEventSerializer(serializers.Serializer):
    venue = serializers.CharField(max_length=100)
    capacity = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.venue = validated_data.get('venue', instance.venue)
        instance.save()
        return instance

class ListEventSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True) 
    class Meta:
        model = Events
        fields = ('title', 'description', 'date', 'time', 'venue', 'capacity', 'organiser', 'tags')  

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta :
        model = Registrations
        fields = ['studentId', 'name', 'email', 'department', 'year']


class ViewEventAttendanceSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = ['studentId', 'name', 'attendance']

class EditEventAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = ['studentId','attendance']

class ViewEventFeedbackSerialiszer(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = ['studentId','name','feedback']

class EditEventFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = ['studentId','feedback']
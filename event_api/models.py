from django.db import models

# Create your models here.

class Tag(models.Model):
     tag_name = models.CharField(max_length = 50, unique=True)

     def __str__(self):
          return self.tag_name
 
class  Events(models.Model):
     title = models.CharField( max_length=150)
     description  = models.CharField(max_length=500)
     date = models.DateField()
     time = models.TimeField()
     venue = models.CharField(max_length=100, default='uknown venue')
     capacity = models.IntegerField()
     organiser = models.CharField(max_length=100)
     tags = models.ManyToManyField(Tag , related_name ="event_tag")

     def  __str__(self):
        return self.title

class Registrations(models.Model):
     event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name = 'registrations')
     studentId = models.CharField(max_length=100)
     name = models.CharField(max_length=100)
     email = models.EmailField()
     department = models.CharField(max_length =100)
     year = models.IntegerField()

     def __str__(self):
          return f"{self.name} - {self.event.title}"
from django.contrib import admin
from .models import Events ,  Tag , Registrations
# Register your models here.

admin.site.register(Events)
admin.site.register(Tag)
admin.site.register(Registrations)
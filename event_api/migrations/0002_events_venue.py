# Generated by Django 5.1.4 on 2024-12-18 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='venue',
            field=models.CharField(default='uknown venue', max_length=100),
        ),
    ]

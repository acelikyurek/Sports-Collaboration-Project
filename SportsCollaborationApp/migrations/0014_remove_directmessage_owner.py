# Generated by Django 3.2.6 on 2021-12-06 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SportsCollaborationApp', '0013_directmessage_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directmessage',
            name='owner',
        ),
    ]

# Generated by Django 2.2 on 2019-04-12 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_delete_programticket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConferenceTicket',
        ),
    ]
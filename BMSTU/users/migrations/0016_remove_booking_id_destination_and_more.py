# Generated by Django 4.2.3 on 2023-07-19 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0015_alter_booking_destination_alter_booking_student"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="id_destination",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="id_student",
        ),
    ]

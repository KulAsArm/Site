# Generated by Django 4.2.3 on 2023-07-18 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_booking"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="id_destination",
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name="booking",
            name="id_student",
            field=models.IntegerField(default=None),
        ),
    ]
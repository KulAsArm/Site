# Generated by Django 4.2.3 on 2023-07-18 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("holidays", "0001_initial"),
        ("users", "0014_booking_id_destination_booking_id_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="destination",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="holidays.destinations",
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="student",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.student",
            ),
        ),
    ]

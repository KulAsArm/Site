# Generated by Django 4.2.3 on 2023-07-17 14:55

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_student_names_of_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="telegram",
            field=models.CharField(
                default=None, max_length=20, validators=[users.models.validate_telegram]
            ),
        ),
    ]

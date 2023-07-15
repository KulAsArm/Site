# Generated by Django 4.2.3 on 2023-07-15 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0008_alter_student_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student",
                related_query_name="student",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_student_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

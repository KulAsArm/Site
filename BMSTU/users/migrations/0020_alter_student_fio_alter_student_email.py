# Generated by Django 4.2.1 on 2023-07-19 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_booking_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='FIO',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]

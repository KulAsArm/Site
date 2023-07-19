from django.db import models
from django.core.exceptions import ValidationError
import re
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from holidays.models import Destinations


# Create your models here.

def validate_phone(value):
    reg = "^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
    if not re.match(reg, value):
        raise ValidationError(f'Неверный формат ввода телефона {value}')
    else:
        return True


def validate_group(value):
    reg = "([а-я|А-Я]){1,4}[0-9]{1,2}[-]\d{2,3}([б,Б,М,м])?"
    if not re.match(reg, value):
        raise ValidationError(f'Неверный формат ввода группы {value}')
    else:
        return True


def validate_telegram(value):
    reg = "@[a-z|A-Z]{1,}"
    if not re.match(reg, value):
        raise ValidationError(f'Неверный формат ввода аккаунта {value}')
    else:
        return True


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student', related_query_name='student')
    FIO = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=50, null=False)
    phone = models.CharField(max_length=16, validators=[validate_phone])
    group = models.CharField(max_length=8, validators=[validate_group])
    names_of_priority = models.CharField(max_length=500, null=True, default=None)
    telegram = models.CharField(max_length=20, validators=[validate_telegram])

    def __str__(self):
        return self.FIO


@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
    instance.student.save()


class Booking(models.Model):
    # id_student = models.IntegerField(default=None, unique=True)
    # id_destination = models.IntegerField(default=None, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (self.student, self.destination)
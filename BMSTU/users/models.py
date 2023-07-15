from django.db import models
from django.core.exceptions import ValidationError
import re
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


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


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FIO = models.CharField(max_length=100, unique=True, null=False)
    email = models.EmailField(max_length=50, unique=True, null=False)
    phone = models.CharField(max_length=16, validators=[validate_phone])
    group = models.CharField(max_length=8, validators=[validate_group])

    def __str__(self):
        return self.FIO


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()
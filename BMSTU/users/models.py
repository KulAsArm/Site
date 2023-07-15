from django.db import models
from django.core.exceptions import ValidationError
import re


# Create your models here.

def validate_phone(value):
    reg = "^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
    if not re.match(reg, value):
        raise ValidationError(f'Неверный формат ввода телефона {value}')
    else:
        return True


def validate_group(value):
    reg = "([а-я|А-Я]){2,4}[0-9]{1,2}[-]\d{2,3}([б,Б,М,м])?"
    if not re.match(reg, value):
        raise ValidationError(f'Неверный формат ввода группы {value}')
    else:
        return True


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    FIO = models.CharField(max_length=100, unique=True, null=False)
    email = models.EmailField(max_length=50, unique=True, null=False)
    phone = models.CharField(max_length=16, validators=[validate_phone])
    group = models.CharField(max_length=8, validators=[validate_group])

    def __str__(self):
        return self.FIO

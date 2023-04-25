from django.db import models
import random
from django.core.validators import MaxValueValidator, MinValueValidator

class FourDigitIDField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['editable'] = False
        kwargs['unique'] = True
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if add:
            value = random.randint(1000, 9999)
            while model_instance.__class__.objects.filter(pk=value).exists():
                value = random.randint(1000, 9999)
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)

class Player(models.Model):
    id = FourDigitIDField(primary_key=True)
    word = models.CharField(max_length=50,unique=True)
    score = models.IntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.word}"

class Computer(models.Model):
    word = models.CharField(max_length=50)
    score_value = models.IntegerField()

    def save(self, *args, **kwargs):
        self.score = len(self.word) * 100
        super().save(*args, **kwargs)

    def __str__(self):
        return self.word


# Create your models here.

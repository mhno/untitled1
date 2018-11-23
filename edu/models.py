from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.Model.OneToOneField(
        User.objects,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    user_bio = models.CharField()

    morf = models.BooleanField(default=False)
from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from users.models import User

# Create your models here.
class Team(models.Model):
    owner = models.OneToOneField(User,related_name='teams_owner')
    operators = models.ManyToManyField(User,related_name='teams_operators',through="Operator")

class Operator(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    Operator = models.OneToOneField(User,on_delete=models.CASCADE,related_name = "operator",primary_key= True)
    active = models.BooleanField(default = True)
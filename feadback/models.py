from django.db import models
from ..home.models import Doctors

# Create your models here.
class Feadback(models.Model):
    fead_dec=models.TextField()
    fead_doc=models.ForeignKey(Doctors,on_delete=models.CASCADE)
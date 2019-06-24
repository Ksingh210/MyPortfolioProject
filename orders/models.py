from django.db import models

class Order(models.Model):
    store = models.CharField(max_length=100)
    time = models.DateTimeField()
    gardensoil = models.BooleanField(default=False)
    pottingmix = models.BooleanField(default=False)
    raisedbed = models.BooleanField(default=False)


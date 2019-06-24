from django.db import models

class Order(models.Model):
    store = models.CharField(max_length=100)
    time = models.DateTimeField()
    gardensoil = models.BooleanField(default=False)
    gardensoilpallets = models.CharField(max_length=2, default=0)
    pottingmix = models.BooleanField(default=False)
    pottingmixpallets = models.CharField(max_length=2, default=0)
    raisedbed = models.BooleanField(default=False)
    raisedbedpallets = models.CharField(max_length=2, default=0)


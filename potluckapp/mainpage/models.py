from django.db import models


class PotluckData(models.Model):
    dish = models.CharField(max_length=200)
    qty = models.CharField(max_length=200)
    takenby = models.CharField(max_length=200)

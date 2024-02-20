from django.db import models

from simple_history.models import HistoricalRecords
class Medicament(models.Model):
 name = models.CharField(max_length=100)
 quantity = models.IntegerField()
 price = models.IntegerField()
 expirationDate= models.DateField()
 typee = models.ForeignKey('Typee', on_delete=models.CASCADE,)
 history = HistoricalRecords()



 def __str__(self) -> str:
    return self.name


class Typee(models.Model):
    Ntype = models.CharField(max_length=100)
    descri = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Ntype


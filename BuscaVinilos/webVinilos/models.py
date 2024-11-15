from django.db import models

class Vinilo(models.Model):
    artista = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=40, decimal_places=2)
    comuna = models.CharField(max_length=100)
    tienda = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.artista} - {self.album}"

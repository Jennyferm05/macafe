from django.db import models


class Venta(models.Model):
    nombre_comprador = models.CharField(max_length=255)
    documento = models.IntegerField()
    fecha_compra = models.DateField(null=True, blank=True)
    producto = models.CharField(max_length=255)
    precio_kilogramo = models.FloatField()
    cantidad = models.IntegerField()
    total_pagar = models.FloatField()

    def __str__(self):
        return f"Venta: {self.id}"

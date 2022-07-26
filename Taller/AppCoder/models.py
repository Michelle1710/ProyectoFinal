from datetime import datetime
from mailbox import NoSuchMailboxError
from tkinter.tix import INTEGER
from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    marca_de_carro = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    placa= models.UUIDField( primary_key=True) 
    email= models.EmailField()
    descripcionRev= models.TextField()

class Estado_revision(models.Model):
    placa = models.IntegerField()
    entrada = models.DateTimeField()
    tipo_reparacion = models.CharField(max_length=20)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Ready'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')

class Entrega_reparacion(models.Model):
    placa = models.IntegerField()
    descripcion =models.TextField()
    entrega= models.DateField()
    status= models.BooleanField()

    def __str__(self) -> str:
        return f"Información: {self.placa} entregado {self.entrega} trabajo realizado {self.descripcion}"


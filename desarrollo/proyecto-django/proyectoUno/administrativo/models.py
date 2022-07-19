from django.db import models

# Create your models here.

class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()

    tipo_opciones = (('Ecuatoriana','Ecuatoriana'), 
                    ('Peruana','Peruana'),
                    ('Colombiana','Colombiana'))
    
    nacionalidad = models.CharField(max_length=30 ,choices=tipo_opciones)

    def __str__(self):
        return "%s %s %d %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)

class Departamento(models.Model):
    costo = models.DecimalField(max_digits=100, decimal_places=2)
    numero_cuartos = models.IntegerField()
    numero_banos = models.IntegerField()
    valor_alicuota = models.DecimalField(max_digits=100, decimal_places=2)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="los_departamentos")

    def __str__(self):
        return "%s %s %s %s %s" % (self.costo,
                self.numero_cuartos,
                self.numero_banos,
                self.valor_alicuota,
                self.propietario)

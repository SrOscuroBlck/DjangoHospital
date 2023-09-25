from django.db import models

# Create your models here.

class Hospital(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    def __str__(self):
        return self.fecha
    
class Consulta(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    def __str__(self):
        return self.fecha
    
class Receta(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    def __str__(self):
        return self.fecha
    



class Meta:
    db_table = 'hospital'
    db_table = 'medico'
    db_table = 'paciente'
    db_table = 'cita'
    db_table = 'consulta'
    db_table = 'receta'

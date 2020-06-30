from django.db import models

# Create your models here.

class tarea_n(models.Model):
    nombre = models.CharField(max_length=150)
    contenido = models.CharField(max_length=300)
    empezado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de inicio')
    fecha_limite = models.DateTimeField(blank=True, null=True,verbose_name='Fecha limite',help_text = "YYYY-MM-DD")
    estado = models.BooleanField(default=0)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
    
    def __str__(self):
        return self.nombre
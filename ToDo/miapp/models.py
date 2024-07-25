from django.db import models

# Create your models here.

class Homework(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    status = models.BooleanField(verbose_name='¿Completado?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')


    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'


    def __str__(self):
        if self.status:
            status = "(Concluido)"
        else:
            status = "(Pendiente)"

        return f"{self.title} {status}"
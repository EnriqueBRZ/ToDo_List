from django.contrib import admin
from .models import Homework

class HomeworkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

# Register your models here.
admin.site.register(Homework, HomeworkAdmin)

# Configurar el título del Panel
title = 'Proyecto To Do List'
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Gestión de Tareas"
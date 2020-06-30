from django.contrib import admin
from ParraWebApp.models import tarea_n

# Register your models here.
class tareaadmin(admin.ModelAdmin):
    list_display=("nombre","contenido","empezado","fecha_limite","estado")
    search_fields = ("nombre","empezado","fecha_limite")
    list_filter = ("nombre","empezado","fecha_limite")

admin.site.register(tarea_n,tareaadmin)


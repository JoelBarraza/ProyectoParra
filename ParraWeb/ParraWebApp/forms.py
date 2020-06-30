from django import forms

from .models import tarea_n

class tareaform(forms.ModelForm):
    class Meta:
        model = tarea_n
        fields = [
            "nombre",
            "contenido",
            "fecha_limite",
        ]
        
class tareatermin(forms.ModelForm):
    class Meta:
        model = tarea_n
        fields = [
            "estado",
        ]

from django import forms
from django.core.exceptions import ValidationError
from .models import Photo
from .settings import BADWORDS

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):
        """Valida si en la descripción se pusieron
        las palabras prohibidas
        :return: diccionario con los atributos si OK
        """
        cleaned_data = super(PhotoForm, self).clean()

        description = cleaned_data.get('description', '')

        for badw in BADWORDS:
            if badw.lower() in description.lower():
                raise ValidationError('La palabra {0} no está permitida'.format(badw))

        # si todo va OK, se devuelve los datos limpios/normalizados
        return cleaned_data
from django.forms import ModelForm
from .models import Elogio


class FormElogio(ModelForm):

    def clean(self):
        data = self.cleaned_data
        comentario = data.get('comentario')


    class Meta:
        model = Elogio
        fields = ('comentario',)
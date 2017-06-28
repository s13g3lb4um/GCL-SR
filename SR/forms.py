from django import forms
from .models import Speech_Recognition


class create_sr(forms.ModelForm):

    class Meta:
        model = Speech_Recognition
        fields = ['audioFile', 'description']

    def __init__(self, *args, **kwargs):
        super(create_sr, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = 'form-control'

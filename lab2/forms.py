from django import forms
from .models import Measurment


class PostForm(forms.ModelForm):
    class Meta:
        model = Measurment
        fields = ('area', 'station', 'date_field' , 'time_field', 'm1' , 'm2' , 'm3', 'm4')
from django import forms
from .models import Measurment, Areas, Area_inform


class MeasurmentForm(forms.ModelForm):
    class Meta:
        model = Measurment
        fields = ('area', 'station', 'date_field' , 'time_field', 'm1' , 'm2' , 'm3', 'm4')



class AreasForm(forms.ModelForm):
    class Meta:
        model = Areas
        fields = ("area", "area_name")




class AreaInformForm(forms.ModelForm):
    class Meta:
        model = Area_inform
        fields = ("areas", "station", "elevation", "point_x", "point_y")

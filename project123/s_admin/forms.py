from django import forms
from s_admin.models import StateModel,CityModel,AreaOperations,Restrotype

class stateForm(forms.ModelForm):
    class Meta:
        model = StateModel
        fields = '__all__'
        labels = {"sname":"Statename"}

class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = '__all__'
        labels = {"cname":"cityname"}

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaOperations
        fields ='__all__'

class RestroFrom(forms.ModelForm):
    class Meta:
        model = Restrotype
        fields = '__all__'

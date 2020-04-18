from django import forms
from restaurent.models import RegistrationFrom

class restarentForm(forms.ModelForm):
    restro_password = forms.CharField(max_length=30,widget=forms.PasswordInput())
    class Meta:
        model = RegistrationFrom
        fields = '__all__'
        exclude = ('otp',)




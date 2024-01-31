from django import forms 
from .models import vfn

class AddForm(forms.ModelForm):
    class Meta:
        model=vfn
        
        fields=('firstname','lastname','email','phone','password','conform_password','gender')


        widgets={
           'firstname':forms.TextInput(attrs={'class':'form-contro'}),
           'lastname':forms.TextInput(attrs={'class':'form-contro'}),
           'email':forms.TextInput(attrs={'class':'form-contro'}),
           'phone':forms.TextInput(attrs={'class':'form-contro'}),
           'password':forms.TextInput(attrs={'class':'form-contro'}),
           'conform_password':forms.TextInput(attrs={'class':'form-contro'}),
           'gender':forms.TextInput(attrs={'class':'form-contro'}),
    }
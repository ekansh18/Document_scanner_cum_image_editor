from django import forms
from .models import Upload

  
class UpForm(forms.ModelForm):
    class Meta:
        model= Upload
        fields = ['image', 'action']
        
           
class UpImage(forms.ModelForm):
    class Meta:
        model=Upload
        fields=['image', 'action']     

class Scup(forms.ModelForm):
    class Meta:
        model=Upload
        fields=['image','sca']              
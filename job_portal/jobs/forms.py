from django import forms 
from .models import Job, Application, Profile

class JobForm(forms.ModelForm):
    class Meta:
        model = Job 
        fields = ['title', 'company', 'location', 'description']
        
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume']
        widgets = {
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['resume']
from django import forms
from .models import New

class UploadNews(forms.ModelForm):
    
    class Meta:
        model = New
        fields = ['title', 'image', 'category', 'news', 'headline', 'breaking','trending','author']

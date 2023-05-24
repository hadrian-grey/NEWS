from django import forms
from .models import News

class UploadNews(forms.ModelForm):
    
    class Meta:
        model = News
        fields = ['title', 'image', 'category', 'news', 'headline', 'breaking','trending']

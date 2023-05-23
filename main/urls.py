from django.urls import path
from .views import Homepage,Upload


urlpatterns=[
    path('',Homepage,name='home'),
    path('upload/',Upload,name='upload')
]
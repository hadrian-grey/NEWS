from django.urls import path
from .views import Homepage,Upload,Detail


urlpatterns=[
    path('',Homepage,name='home'),
    path('upload/',Upload,name='upload'),
    path('detail/<int:pk>/',Detail,name='detail'),
]
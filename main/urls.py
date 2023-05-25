from django.urls import path
from .views import Homepage,Detail


urlpatterns=[
    path('',Homepage,name='home'),
    path('detail/<int:pk>/',Detail,name='detail'),
]
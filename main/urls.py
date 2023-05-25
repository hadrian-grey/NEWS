from django.urls import path
from .views import Homepage,Detail,privacy


urlpatterns=[
    path('',Homepage,name='home'),
    path('detail/<int:pk>/',Detail,name='detail'),
    path('policies/privacy/',privacy,name='privacy')
]
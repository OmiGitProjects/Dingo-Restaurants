from django.urls import path
from .import views

urlpatterns = [
        path('', views.contactInfo, name='ContactInfo')
]

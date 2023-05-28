from django.urls import path
from .views import  accueil_view
from .views import  register
from .views import  profil_view





urlpatterns = [
   
    path('', accueil_view, name='accueil'),
    path('register/',register, name = 'register'),
    path('profil/', profil_view, name ='profil'),
 
]

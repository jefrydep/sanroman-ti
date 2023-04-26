from django.urls import path, re_path

from proyecto_tariachi import views

urlpatterns = [
    path('',views.home,name='tariachi')
    
    
]
from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [
    path('',views.ver_index,name='ver_index'),
    path('index.html',views.ver_index,name='ver_index'),
    path('listar_productos.html', views.ver_productos, name='ver_productos'),
    path('Registro.html', views.register, name='register'),
    path('Contactenos.html', views.ver_contactenos, name='ver_contactenos'),
    path('Mision&Vision.html', views.ver_mision, name='ver_mision'),
    path('QuienesSomos.html', views.ver_quienes, name='ver_quienes'),
    path('Login.html', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('reset_password.html', views.pass_reset, name='pass_reset'),
    path('password_reset_done.html', views.pass_reset2, name='pass_reset2'),
    path('password_reset_email.html', views.pass_reset3, name='pass_reset3'),
    path('password_reset_confirm', views.pass_reset4, name='pass_reset4'),
    path('password_reset_complete', views.pass_reset5, name='pass_reset5'),

    
]
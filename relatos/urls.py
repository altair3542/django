from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relatos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', views.registro_usuario, name='registro'),
    path('', views.home, name='home'),
    path('acerca/', views.acerca, name='acerca'),
    path('relatos/', views.lista_relatos, name='lista_relatos'),
    path('relatos/agregar/', views.agregar_relato, name='agregar_relato'),
    path('relatos/<int:relato_id>/', views.detalle_relato, name='detalle_relato'),

]

from django.urls import path
from . import views

app_name = 'contacto'

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('faq/', views.faq, name='faq'),
]

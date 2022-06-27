from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('comment/', views.comment, name='comment'),
    path('success/', views.success, name='success')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login),
    path('myaccount/', views.grafana),
    path('dashboard/', views.setpreferences)
]
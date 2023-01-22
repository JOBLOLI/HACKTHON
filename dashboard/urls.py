from django.urls import path
from . import views

urlpatterns = [
    path('myaccount/', views.firstview),
    path('', views.firstview)
]
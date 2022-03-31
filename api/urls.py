from django.urls import path
from . import views
urlpatterns = [
    path('', views.getDate),
    path('add/', views.addItem)
]

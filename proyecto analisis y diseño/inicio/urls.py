from django.urls import path
from . import views
urlpatterns = [
    path('', views.hol),
    path('about/', views.hol2)
]

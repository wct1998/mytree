from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainmenu, name="login")
]
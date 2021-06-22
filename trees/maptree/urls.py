from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'maptree'
urlpatterns = [
    path('lists/', views.maplist, name='lists'),
    path('insert/', views.map_insert, name='insert')
    # path('lists/', mapview.as_view(), name="maptrees")
]
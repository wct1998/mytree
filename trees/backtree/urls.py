from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'backtree'
urlpatterns = [
    # path('', views.hello),
    # path('lists/<pindex>', views.lists,name='lists'),
    url(r'^lists(?P<pIndex>[0-9]*)/$', views.lists, name='lists'),
    path('check/', views.checktree, name='check'),
    path('codes/', views.codes, name='codes'),
    path('user/', views.usertree, name='user'),
    path('structure', views.structure_edit, name='structure')
    # path('insert/', views.insert,name='insert'),

    # url('index/', views.lists, name='lists'),
    # url('index/', views.insert, name='insert'),
    # url('index/', views.hello),
]
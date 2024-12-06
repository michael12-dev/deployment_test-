from django.urls import path
from . import views
urlpatterns= [
    path('', views.index, name='index'),
    path('worldview', views.worldview, name = 'worldview' )
]
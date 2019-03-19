from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index3'),
	path('nex', views.next, name='next3'),
]


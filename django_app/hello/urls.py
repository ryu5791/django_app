from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index3'),
	path('form_', views.form, name='form1'),
]


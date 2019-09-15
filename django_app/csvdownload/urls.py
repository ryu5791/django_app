from django.urls import path
from . import views

app_name = 'csvdownload'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('import/', views.PostImport.as_view(), name='import'),
    path('export/', views.PostExport, name='export'),
]

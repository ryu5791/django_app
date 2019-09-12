from django.conf.urls import url
from .views import HelloView1

urlpatterns = [
	url(r'', HelloView1.as_view(), name='index5'),
]


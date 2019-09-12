from django.conf.urls import url
from .views import InputView

urlpatterns = [
	url(u'', InputView.as_view(), name='index2'),
]


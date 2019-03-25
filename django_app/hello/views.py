from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index1(request):
	data5 = Friend.objects.all()
	params = {
			'title20':		'Hello',
			'message20':	'all friends.',
			'data20':		data5,
		}
	return render(request, 'hello/index.html', params)


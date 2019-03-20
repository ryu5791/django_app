from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	params = {
		'title'	:'Hello/Index',
		'msg10'	:'これは、サンプルで作ったページです。',
	}
	return render(request, 'hello/index.html', params)

def form(request):
	msg9 = request.POST["msg5"]
	params = {
		'title'	:'Hello/Form',
		'msg10'	:'こんにちは、'+msg9+'さん。',
	}
	return render(request, 'hello/index.html', params)



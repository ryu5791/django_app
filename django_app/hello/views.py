from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm

def index(request):
	params = {
		'title20'		:'Hello',
		'message20'		:'your data:',
		'form20'		:HelloForm(),
	}
	if (request.method == 'POST'):
		params['message20'] = '名前：' + request.POST['name1'] + \
			'<br>メール：' + request.POST['mail1'] + \
			'<br>年齢：' + request.POST['age1']
		params['form20'] = HelloForm(request.POST)
	return render(request, 'hello/index.html', params)


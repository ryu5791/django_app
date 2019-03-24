from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):

	def __init__(self):
		self.params = {
			'title20'		:'Hello',
			'message20'		:'your data:',
			'form20'		:HelloForm(),
		}

	def get(self, request):
		return render(request, 'hello/index.html', self.params)

	def post(self, request):
		msg = 'あなたは、<b>' + request.POST['name1'] + \
			'(' + request.POST['age1'] + \
			')</b>さんです。<br>メールアドレスは<b>' + request.POST['mail1'] + \
			'</b>ですね。'
		self.params['message20'] = msg
		self.params['form20'] = HelloForm(request.POST)
		return render(request, 'hello/index.html', self.params)


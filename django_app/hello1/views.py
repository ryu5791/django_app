from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
import logging

#@login_required(login_url='/admin/login/')
class HelloView1(TemplateView):

	testDt = 5

	def __init__(self):
		self.params = {
			'title20'	:'Helloo',
			'message20'	:'your data--:',
			'form20'	:HelloForm(),
		}

		logging.debug(HelloForm())
		logging.debug(self.params['form20'])


	def get(self, request):
	
		testDt = 3
		
		logging.debug("testDt:")
		logging.debug(testDt)
		logging.debug("self.testDt:")
		logging.debug(self.testDt)
	
		testcls = TestClass()
		logging.debug("testcls.testdt1:")
		logging.debug(testcls.testdt1)

		dt = render(request, 'hello1/index.html', self.params)
		logging.debug("get:dt:")
		logging.debug(dt)
		return dt
#		return render(request, 'hello1/index.html', self.params)

	def post(self, request):
		msg = 'あなたは、<b>' + request.POST['name1'] + \
			'(' + request.POST['age1'] + \
			')</b>さんです。<br>メールアドレスは<b>' + request.POST['mail1'] + \
			'</b>ですね。'
		self.params['message20'] = msg
		self.params['form20'] = HelloForm(request.POST)
		dt = render(request, 'hello1/index.html', self.params)
		logging.debug("post:dt:")
		logging.debug(dt)
		return dt
#		return render(request, 'hello1/index.html', self.params)


class TestClass():

	testdt1 = 5
	testdt2 = 7



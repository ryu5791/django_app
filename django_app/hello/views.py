from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
import logging
import json
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):

	def __init__(self):
#		temp = open('Score2019_1.json',encoding="utf-8_sig")
#		tbl_score = json.load(temp)
#		logging.debug(num)

		data5 = Friend.objects.all()
		self.params = {
			'title20'		:'Hello',
			'message20'		:'your data:',
			'data20':		data5,
			
		}

	def get(self, request):
		return render(request, 'hello/index.html', self.params)

'''	def post(self, request):
		msg = 'あなたは、<b>' + request.POST['name1'] + \
			'(' + request.POST['age1'] + \
			')</b>さんです。<br>メールアドレスは<b>' + request.POST['mail1'] + \
			'</b>ですね。'
		self.params['message20'] = msg
		self.params['form20'] = HelloForm(request.POST)
		return render(request, 'hello/index.html', self.params)
'''
'''
def index1(request):


	temp = open('Score2019_1.json',encoding="utf-8_sig")
	tbl_score = json.load(temp)

	num=0
	for src in tbl_score["results"]:
		num += 1

	logging.debug(num)

	data5 = Friend.objects.all()
	params = {
			'title20':		'Hello',
			'message20':	'all friends.',
			'data20':		data5,
		}
	return render(request, 'hello/index.html', params)
'''

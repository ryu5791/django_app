from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
import logging
import json

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


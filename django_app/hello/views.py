from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	msg = request.GET['msg']
	return HttpResponse('you typed: "' + msg + '".')


from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# from .forms import HelloForm
from .forms import MakeGameRslt

import logging

# Create your views here.
class InputView(TemplateView):

	gameRsltDt = [0,0,0,0,0,0,0]


	def __init__(self):
	
		gameRslt = MakeGameRslt(self.gameRsltDt)
		self.params = {
			'message'	:'test',
			"form20" 	: gameRslt.tblGm
		}
		logging.debug(self.params["form20"])

	def get(self, request):
		logging.debug("test get:")
		logging.debug(request)
		
		try:
		
			logging.debug("field1:" +  request.GET["field1"])
			logging.debug("field2:" +  request.GET["field2"])

			row = int(request.GET["field1"]) - 3
			col = int(request.GET["field2"]) - 1
			
			if self.gameRsltDt[col] == (row+1):
				self.gameRsltDt[col] = 0
			else :
				self.gameRsltDt[col] = (row+1)

			gameRslt = MakeGameRslt(self.gameRsltDt)
			self.params = {
				'message'	:'test',
				"form20" 	: gameRslt.tblGm
			}
			logging.debug(self.params["form20"])

		except KeyError:
			logging.debug("except")

		logging.debug(self.gameRsltDt)

		return render(request, 'score_input/main.html', self.params)

	def post(self, request):
		logging.debug("test post:")
		self.params['message'] = 'aaa'
		return render(request, 'score_input/main.html', self.params)

	def chg_game_pt(self, dt):
		logging.debug("dt:" +  dt)
		if dt == "〇":
			ret = ""
		else:
			ret = "〇"
		logging.debug("ret:" +  ret)
		return ret


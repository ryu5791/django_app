from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import HelloForm

import logging

# Create your views here.
class InputView(TemplateView):

	gameRsltDt = [2,0,0,0,0,0,0]


	def __init__(self):
		cn = HelloForm()
		cn.gameRsltFunc(self.gameRsltDt)
		self.params = {
			'message'	:'test',
			"form20" : cn
		}
		logging.debug(cn)
		logging.debug(HelloForm())
		logging.debug("init")

	def get(self, request):
		logging.debug("test get:")
		logging.debug(request)
		
		try:
		
			logging.debug("field1:" +  request.GET["field1"])
			logging.debug("field2:" +  request.GET["field2"])

			if request.GET["field1"] == "4" \
			  and request.GET["field2"] == "1":
				
#				logging.debug( self.params["game_dt10"] )
				if self.gameRsltDt[0] == 2:
					self.gameRsltDt[0] = 0
				else:
					self.gameRsltDt[0] = 2
				
				logging.debug(self.gameRsltDt)
				
#				self.params["game_dt10"] = self.chg_game_pt(self.params["game_dt10"])
#				logging.debug( self.params["game_dt10"] )

			cl = HelloForm()
			cl.gameRsltFunc(self.gameRsltDt)
			self.params["form20"] = cl
			
#			logging.debug('self.params["form20"]:' + self.params["form20"])
			logging.debug(self.params["form20"])
			logging.debug(self)

#			elif request.GET["field1"] == "3" \
#			  and request.GET["field2"] == "2":
#
#				logging.debug( self.params["game_dt11"] )
#				self.params["game_dt11"] = self.chg_game_pt(self.params["game_dt11"])
#				logging.debug( self.params["game_dt11"] )

		except KeyError:
			logging.debug("except")

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


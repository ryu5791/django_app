from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend, TblScore, TblMember, TblRank
import logging
import json
from django.views.generic import TemplateView
#from .forms import HelloForm
import time
from .views_makeTbl.makeRankTbl import *

class HelloView(TemplateView):

	def __init__(self):

		# 時間計測 開始
		startTime = time.time()
		logging.debug("HelloView/__init__ start time:" + str(startTime))

		i=0
		
#		# スコア → データベース
#		temp = open('Score2019_1.json',encoding="utf-8_sig")
#		json_score = json.load(temp)
#
#		for scr in json_score["results"]:
#			tblScore, created = TblScore.objects.get_or_create(date=scr["date"].replace('/', '-') \
#															,  gameNo=scr["gameNo"] \
#															,  playerID=int(scr["ID"]))
#			tblScore.date = scr["date"].replace('/', '-')
#			tblScore.gameNo		= int(scr["gameNo"])
#			tblScore.gamePt     = int(scr["gamePt"])
#			tblScore.playerID   = int(scr["ID"])
#			tblScore.pairID     = int(scr["pairID"])
#			tblScore.row        = int(scr["row"])
#			tblScore.serve1st   = bool(scr["serve1st"])
#			tblScore.serve2nd   = bool(scr["serve2nd"])
#			tblScore.serveTurn  = int(scr["serveTurn"]-1)
#			i += 1
#			tblScore.save()
#		logging.debug(i)


#		temp = open('member.json',encoding="utf-8_sig")
#		json_member = json.load(temp)
#
#		# メンバー → データベース登録
#		for mem in json_member["results"]:
#			tblMember, created = TblMember.objects.get_or_create(playerID=int(mem["ID"]))
#			tblMember.playerID		= int(mem["ID"])
#			tblMember.name          = mem["name"]
#			tblMember.dispName      = mem["dispName"]
#			tblMember.inputName1    = mem["nickname1"]
#			tblMember.inputName2    = mem["dispName"]
#			tblMember.save()

#		data5 = Friend.objects.all()
#		data5 = TblMember.objects.all()
		data5 = TblRank.objects.all()
		data5 = get_tblRank("2019-01-01", "2019-06-30")
		self.params = {
			'title20'		:'Hello',
			'message20'		:'your data:',
			'data20':		data5,
			
		}

		# 時間計測 終了
		endTime = time.time()
		logging.debug("HelloView/__init__ end time:" + str(endTime))
		logging.debug("HelloView/__init__ process time:" + str(endTime-startTime))


	def get(self, request):
		startTime = time.time()
		logging.debug("HelloView/get start time:" + str(startTime))
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

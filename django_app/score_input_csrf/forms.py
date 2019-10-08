from django import forms
import logging

class MakeGameRslt():

	tblGm=[[""]*2 for i in range(7)]

	def __init__(self, inpTblGm):
		for (outGm, inGm) in zip(self.tblGm, inpTblGm):
			if inGm == 1:
				logging.debug("inGm == 1")
#				outGm = ["◎", ""]
				outGm[0] = "◎"
				outGm[1] = ""
			elif inGm == 2:
				logging.debug("inGm == 2")
#				outGm = ["", "◎"]
				outGm[0] = ""
				outGm[1] = "◎"
			else:
				logging.debug("inGm == 0")
#				outGm = ["", ""]
				outGm[0] = ""
				outGm[1] = ""
			logging.debug(self.tblGm)

class HelloForm(forms.Form):

	gameRslt10 = "〇"
	gameRslt11 = "55"

	def gameRsltFunc(self, gameDt):

		if gameDt[0] == 2:
			self.gameRslt10 = "〇"
		else:
			self.gameRslt10 = ""

		logging.debug(self.gameRslt10)

#	name1 = forms.CharField(label='_name')
#	mail1 = forms.CharField(label='_mail')
#	age1 = forms.IntegerField(label='_age')

class PullDown1(forms.Form):
	menuData = [
		('one', 'item 1'),
		('two', 'item 2'),
		('three', 'item 3'),
	]
	
	choice = forms.ChoiceField(label='Choice', \
			choices=menuData)

class PullDown2(forms.Form):
	menuData = [
		('one', 'item 1'),
		('two', 'item 2'),
		('three', 'item 3'),
		('four', 'item 4'),
	]
	
	choice = forms.ChoiceField(label='Choice', \
			choices=menuData)





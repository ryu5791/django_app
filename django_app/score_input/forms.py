from django import forms
import logging

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





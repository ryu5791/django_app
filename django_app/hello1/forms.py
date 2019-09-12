from django import forms

class HelloForm(forms.Form):
	name1 = forms.CharField(label='_name')
	mail1 = forms.CharField(label='_mail')
	age1 = forms.IntegerField(label='_age')



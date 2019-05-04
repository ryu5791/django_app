from django.db import models

# Create your models here.

class Friend(models.Model):
	name = models.CharField(max_length=100)
	mail = models.EmailField(max_length=200)
	gender = models.BooleanField()
	age = models.IntegerField(default=0)
	birthday = models.DateField()
	
	def __str__(self):
		return '<Friend:id=' + str(self.id) + '< ' + \
			self.name + '(' + str(self.age) + ')>'

class TblScore(models.Model):
	date		= models.DateField(null=True)
	gameNo		= models.PositiveIntegerField(null=True)
	gamePt		= models.PositiveIntegerField(default=0, null=True, blank=True)
	playerID	= models.PositiveIntegerField(default=0, null=True)
	pairID		= models.PositiveIntegerField(default=0, null=True)
	row			= models.PositiveIntegerField(default=0, null=True)
	serve1st	= models.BooleanField(default=False, null=True)
	serve2nd	= models.BooleanField(default=False, null=True)
	serveTurn	= models.PositiveIntegerField(default=0, null=True)
	updateDate	= models.DateTimeField( default='2019-05-01 20:29:39', null=True)

class TblMember(models.Model):
	playerID	= models.PositiveIntegerField()
	name		= models.CharField(default="", blank=True, max_length=20)
	dispName	= models.CharField(default="", blank=True, max_length=20)
	inputName1	= models.CharField(default="", blank=True, max_length=20)
	inputName2	= models.CharField(default="", blank=True, max_length=20)

class TblRank(models.Model):
	gameNum		= models.PositiveIntegerField()
	gamePt		= models.FloatField()
	gross		= models.FloatField()
	HDCP		= models.FloatField()
	playerID	= models.PositiveIntegerField()
	name		= models.CharField(default="", max_length=20)
	net			= models.FloatField()
	winNum		= models.PositiveIntegerField()

class TblDaily(models.Model):
	date		= models.DateField(null=True)
	totalGame	= models.PositiveIntegerField()


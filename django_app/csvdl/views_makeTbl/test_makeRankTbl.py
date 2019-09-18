import unittest
import pytest
from .hello.views_makeTbl.makeRankTbl import *

#class TestManageRank():
#	def test_get(self):
#		rank = makeRankTbl.ManageRank()
#		assert rank.get("2019-01-01", "2019-01-01")

def test_get_nameFromId(playerID, tMember):
	assert makeRankTbl.get_nameFromId(1, TblMember.objects.filter())



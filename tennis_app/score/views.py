from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import logging

@login_required(login_url='/admin/login/')
def index(request):
    test = User.objects.filter(username=request.user)
    logging.debug("index user:" + str(request.user))
    logging.debug("index is_super:" + str(request.user.is_superuser))
    logging.debug("index test:" + str(test))
    logging.debug("index has_perm:" + str(request.user.has_perm("score.add_tblscore") ))
#   logging.debug("index has_perm:" + str(request.user.has_perm("auth.add_user") ))
    params = {'login_user': request.user,}
    return render(request, "score/index.html", params)



# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseForbidden
from django.shortcuts import render


def index_view(request):
	return render(request, 'index.html', {})

def audio_post_view(request):
	# prohibit get requests at this url/view
	# if request.method == "GET":
	# 	return HttpResponseForbidden()

	print "beginning of post--------------------"
	print request.POST
	print "end of post--------------------" 






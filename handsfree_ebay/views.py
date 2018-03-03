# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseForbidden
from django.shortcuts import render

import requests


def index_view(request):
	return render(request, 'index.html', {})

def audio_post_view(request):
	# prohibit get requests at this url/view
	if request.method == "GET":
		return HttpResponseForbidden()

	# print "beginning of post--------------------"
	uploadedFile = open("sample.wav", "wb") 
	# uploadedFile.write(request.body);
	# uploadedFile.close()

	# print request.POST
	# print request.FILES
	# # response = requests.get(request.POST.get("audioURL"))
	# # print "the response: ", request.content
	# print "request body: ", request.body

	# print "end of post--------------------" 
	return render(request, 'index.html', {})





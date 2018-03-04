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

	# response = call_bing_api(request.body)
	

	return render(request, 'index.html', {})





# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseForbidden, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
# from django.core.cache import cache 

import requests


def index_view(request):
	return render(request, 'index.html', {})

def audio_post_view(request):
	# prohibit get requests at this url/view

	# response = HttpResponse(content_type='application/octet-stream')

	# if not request.COOKIES.get("user_id"):
	# 	response.set_cookie("user_id", "0", 300) # 5 minute cache expiry 
	# else:
	# 	new_user_id = int(request.COOKIES.get('user_id', "0")) + 1 
	# 	response.set_cookie("user_id", str(new_user_id) + 300)
		
	# # audio_bytes = call_bing_api(request.body, request.COOKIES.get("user_id"))
	audio = None
	# with open("audio_out.mp3", "rb") as f:
		# f.write(request.body)
		# audio = f.read()
	
	# response["body"] = audio
	# return "fuck"
	# return response
	# print audio
	url = "/media/audio/audio_out.mp3"
	response =  HttpResponse(url, content_type='application/octet-stream')
	# response["Access-Control-Allow-Origin"] = "*."
	return response
	 
	# return render(request, 'index.html', {})

# HttpResponse(data, )







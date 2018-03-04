# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseForbidden, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from handsfree_ebay.services import handsfree
# from uuid import uuid4
# from django.core.cache import cache 

import requests


def index_view(request):
	return render(request, 'index.html', {})

def audio_post_view(request):

	response = HttpResponse(content_type='text/html')

	if not request.COOKIES.get("user_id"):
		response.set_cookie("user_id", "0", 300) # 5 minute cache expiry 
	else:
		new_user_id = int(request.COOKIES.get('user_id', "0")) + 1 
		response.set_cookie("user_id", str(new_user_id) + 300)
		
	audio_bytes, state = handsfree.provide_search_terms(request.body, 
								request.COOKIES.get("user_id"))
	
	file_name = "voice-assist-audio.mp3" 
	with open(file_name, "wb") as f:
		f.write(audio_bytes)
	
	fil_url = "/media/audio/" + file_name
	response["body"] = fil_url
	
	return response
	







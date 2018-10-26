from django.shortcuts import render
from .models import *

def home(request, flipper):
	if request.method == 'GET':
		post = Post.objects.get(id=flipper)
		post_list = [post, post, post, post, post]
		return render(request, 'blog/home.html', {'aerhgui':post_list})

def home2(request):
	return render(request, 'blog/home2.html')
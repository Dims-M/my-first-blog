
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request):
	#return HttpResponse(request, 'blog/post_list.html', {})
	return render(request, 'blog/post_list.html', {})
	

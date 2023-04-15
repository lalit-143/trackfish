from django.shortcuts import render, redirect, HttpResponse
from fishapp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

# Create your views here.



def home(request, url, uid):
	web_obj = WebsiteLink.objects.get(id = uid)
	mylink = web_obj.link
	data = { 'myurl' : mylink }
	return render(request, 'home1.html', data)


def home2(request, url):
	return render(request, 'home2.html')


@csrf_exempt
def save_location(request, lat, lng):
	obj = Location(
		lat = lat,
		lng = lng,)
	obj.save()
	return HttpResponse("success")

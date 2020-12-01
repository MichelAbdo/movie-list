from django.shortcuts import render
from django.http import HttpResponse
from .helper import Helper

def index(request):
    helper = Helper()
    movies_people_response = helper.get_movies_people()
    return HttpResponse(movies_people_response)

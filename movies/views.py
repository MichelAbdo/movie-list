from django.shortcuts import render
from django.http import HttpResponse
from .movies_service import MoviesService

def index(request):
    movies_service = MoviesService()
    movies_people_response = movies_service.get_movies_people()
    return HttpResponse(movies_people_response)

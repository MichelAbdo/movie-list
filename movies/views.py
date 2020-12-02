from django.shortcuts import render
from .movies_service import MoviesService

def index(request):
    movies_service = MoviesService()
    movies_people_list = movies_service.get_movies_people()

    context = {'movies_people_list': movies_people_list}
    return render(request, "movies/index.html", context)

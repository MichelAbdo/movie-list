from django.shortcuts import render
from .movies_service import MoviesService
from django.core.cache import cache


def index(request):
    movies_people_list: list = cache.get('movies_people_list')
    if movies_people_list is None:
        movies_people_list = MoviesService().get_movies_people()
        cache.set('movies_people_list', movies_people_list, 60)

    context = {'movies_people_list': movies_people_list}

    return render(request, "movies/index.html", context)

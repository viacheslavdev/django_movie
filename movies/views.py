from django.shortcuts import render
from django.views import View

from movies.models import Movie

class MoviesView(View):
    """ Список фильмов """

    def get(self, request):

        movies = Movie.objects.all()
        return render(request, '../templates/movies/movie_list.html', {'movie_list': movies})

class MovieDetailView(View):
    """ Полное описание фильма """

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        return render(request, '../templates/movies/movie_list.html', {'movie': movie})
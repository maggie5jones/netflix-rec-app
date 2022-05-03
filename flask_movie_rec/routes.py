import requests
from flask import Blueprint, render_template, current_app, request
from ./netflix.py import get_recommendations_new

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    poster_url = 'http://api.themoviedb.ord/3/movie/{imdbid}/images?api_key=1a3b037b3193bfd1535049e30f4d4890'

    movies = []

    if request.method == 'POST':
        #TODO: write things here to incorporate backend code
        results = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        #TODO: loop through items from results
        for result in results:
            movie_data = 10
            movies.append(movie_data)

    return render_template('index.html', movies=movies)
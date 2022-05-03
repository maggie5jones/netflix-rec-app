import requests
from flask import Blueprint, render_template, current_app, request
from ./netflix.py import get_recommendations_new

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    movies = get_recommendations_new(user_input_title)

    if request.method == 'POST':
        #TODO: write things here to incorporate backend code
        results = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        #TODO: loop through items from results
        for result in results:
            movie_data = 10
            movies.append(movie_data)

    return render_template('index.html', movies=movies)

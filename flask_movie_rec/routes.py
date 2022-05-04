import requests
from flask import Blueprint, render_template, current_app, request
# from . import netflix.get_recommendations_new, netflix.get_durations

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    movies = []

    if request.method == 'POST':
        if request.form.get('submit') == 'random':
            results = random_movies() 
        else if request.form.get('submit') == 'query':
            title = request.form.get('query')
            results = get_recommendations_new(title)
        
        for i in range(len(results)):
            movie_data = {
                'id': imdb_id_from_title(results[i]),
                #TODO: url if possible
                'url': '',
                #TODO: poster!
                'poster': '',
                'duration': (get_durations(results))[i],
                'title': results[i],
            }
            movies.append(movie_data)

    return render_template('index.html', movies=movies)

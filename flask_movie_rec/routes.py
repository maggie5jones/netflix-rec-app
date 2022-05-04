import requests
from flask import Blueprint, render_template, current_app, request, url_for
from . import netflix

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    movies = []
    results = []

    if request.method == 'POST':
        if request.form.get('submit') == 'random':
            results = netflix.random_movies() 

            for i in range(len(results)):
                movie_data = {
                    'id': 12345, # netflix.imdb_id_from_title(results[i]),
                    #TODO: url if possible
                    'url': '',
                    'poster': url_for('static', filename='up.png'),
                    'duration': (netflix.get_durations(results))[i],
                    'title': results[i],
                }
                movies.append(movie_data)

        else: # if request.form.get('submit') == 'query'
            title = request.form.get('query')
            results = netflix.get_recommendations_new(title)

            for i in range(len(results)):
                movie_data = {
                    'id': 12345, # netflix.imdb_id_from_title(results[i]),
                    #TODO: url if possible
                    'url': '',
                    'poster': url_for('static', filename='lnx.png'),
                    'duration': (netflix.get_durations(results))[i],
                    'title': results[i],
                }
                movies.append(movie_data)
        
    return render_template('index.html', movies=movies)

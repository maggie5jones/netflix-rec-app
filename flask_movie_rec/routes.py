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
            ids = netflix.imdb_ids_from_title(results)
            durations = netflix.get_durations(results)
            netflix.download_posters(ids)
        else: 
            title = request.form.get('query')
            results = netflix.get_recommendations_new(title)
            ids = netflix.imdb_ids_from_title(results)
            durations = netflix.get_durations(results)
            netflix.download_posters(ids)

        for i in range(len(results)):
            movie_data = {
                'id': ids[i],
                #TODO: url if possible
                'url': '',
                'poster': url_for('static', filename='up.png'), # f'{ids[i]}_img.png'
                'duration': durations[i],
                'title': results[i],
            }
            movies.append(movie_data)
        
    return render_template('index.html', movies=movies)

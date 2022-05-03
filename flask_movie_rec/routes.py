from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    #TODO: write things here to incorporate backend code
    results = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #TODO: loop through items from results
    movies = []
    for result in results:
        movie_data = 10
        movies.append(movie_data)

    return render_template('index.html', movies=movies)
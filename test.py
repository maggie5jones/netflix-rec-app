# import movieposters as mp

# link = mp.get_poster(title='breakfast club')
# link = mp.get_poster(id='tt0088847')  # can also be found using movie's id
# link = mp.get_poster(id=88847)

# print(link)
import pandas as pd

netflix_overall=pd.read_csv("netflix_titles.csv")

tester = ['Til Death Do Us Part', 'Apollo 18', 'Incarnate', 'Black Mirror', 'Transformers: Cyberverse', 'Abby Sen', 'Candyflip', 'Altered Carbon', 'Dark']

def get_durations(titles):
    old = []
    for title in titles:
        #titles = netflix_overall['title'].iloc[movie_indices].tolist()
        found = netflix_overall.loc[netflix_overall['title'] == title]
        dur = found['duration'].tolist()
        old.append(dur)
    durations = [movie for sublist in old for movie in sublist]
    return durations

# testy = netflix_overall.loc[netflix_overall['title'] == 'Inception']
# print(testy['duration'].tolist())

def random_movies():
    movies = []
    for i in range(9):
        movie = netflix_overall.sample()
        movies.append(movie['title'].tolist())
    random = [movie for sublist in movies for movie in sublist]
    return random

print(random_movies())
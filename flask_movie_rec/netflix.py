import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import urllib
import requests
import os
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

netflix_overall=pd.read_csv("netflix_titles.csv")

def random_movies():
    movies = []
    for i in range(9):
        movie = netflix_overall.sample()
        movies.append(movie['title'].tolist())
    random = [movie for sublist in movies for movie in sublist]
    return random

#removing stopwords
tfidf = TfidfVectorizer(stop_words='english')

#Replace NaN with an empty string
netflix_overall['description'] = netflix_overall['description'].fillna('')

#Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(netflix_overall['description'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(netflix_overall.index, index=netflix_overall['title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return netflix_overall['title'].iloc[movie_indices]
  
# new recommedation system??
filledna=netflix_overall.fillna('')

def clean_data(x):
    return str.lower(x.replace(" ", ""))

features=['title','director','cast','listed_in','description']
filledna=filledna[features]

for feature in features:
    filledna[feature] = filledna[feature].apply(clean_data)
    
def create_soup(x):
    return x['title']+ ' ' + x['director'] + ' ' + x['cast'] + ' ' +x['listed_in']+' '+ x['description']  

filledna['soup'] = filledna.apply(create_soup, axis=1)

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(filledna['soup'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

filledna=filledna.reset_index()
indices = pd.Series(filledna.index, index=filledna['title'])

def get_recommendations_new(title, cosine_sim=cosine_sim):
    title=title.replace(' ','').lower()
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 9 most similar movies
    sim_scores = sim_scores[1:10]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    titles = netflix_overall['title'].iloc[movie_indices].tolist()
    return titles

def get_durations(titles):
    old = []
    for title in titles:
        #titles = netflix_overall['title'].iloc[movie_indices].tolist()
        found = netflix_overall.loc[netflix_overall['title'] == title]
        dur = found['duration'].tolist()
        old.append(dur)
    durations = [movie for sublist in old for movie in sublist]
    return durations

# all of the code below is for retrieving the movie poster to display on the front-end

def imdb_ids_from_title(movies):
    imdb_ids = []
    for title in movies:
        url = f"http://www.omdbapi.com/?t={title}&apikey=aa106b0d"

        r = requests.get(url)
        data = r.json()
        if 'imdbID' in data:    
            imdb_id = (data['imdbID']) 
            imdb_ids.append(imdb_id)
        else:
            imdb_ids.append(0)
    return imdb_ids

def download_posters(movies):
    for imdb_id in movies:
        filename = str(imdb_id) + '_img.png'
        save_path = '/Users/Guest/Desktop/181final/flask_movie_rec/static'
        completeName = os.path.join(save_path, filename)

        new_url = f'http://img.omdbapi.com/?i={imdb_id}&apikey=aa106b0d'
        response = requests.get(new_url)

        file = open(completeName, "wb")
        file.write(response.content)
        file.close()

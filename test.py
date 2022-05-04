import requests
# import os

# # tt1772240 = Inception

# imdb_id = 'tt1772240'

# filename = imdb_id + '_img.png'
# save_path = './flask_movie_rec/static'
# completeName = os.path.join(save_path, filename)

# new_url = f'http://img.omdbapi.com/?i={imdb_id}&apikey=aa106b0d'

# response = requests.get(new_url)

# file = open(completeName, "wb")
# file.write(response.content)
# file.close()

# # /Users/Guest/Desktop/181final/flask_movie_rec/static/tt1772240_img.png

url = f"http://www.omdbapi.com/?t=3%&apikey=aa106b0d"

r = requests.get(url)
data = r.json()
imdb_id = (data['imdbID'])

print(imdb_id)

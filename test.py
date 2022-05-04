import requests
import urllib

def imdb_id_from_title(title):
    """ return IMDB id for search string

        Args::
            title (str): the movie title search string

        Returns: 
            str. IMDB id, e.g., 'tt0095016' 
            None. If no match was found

    """
    pattern = 'http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q={movie_title}'
    url = pattern.format(movie_title=urllib.quote(title))
    r = requests.get(url)
    res = r.json()
    # sections in descending order or preference
    for section in ['popular','exact','substring']:
        key = 'title_' + section 
        if key in res:
            return res[key][0]['id']

print(imdb_id_from_title('Inception'))

CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
KEY = '1a3b037b3193bfd1535049e30f4d4890'

url = CONFIG_PATTERN.format(key=KEY)
r = requests.get(url)
config = r.json()

base_url = config['images']['base_url']
sizes = config['images']['poster_sizes']

"""
    'sizes' should be sorted in ascending order, so
        max_size = sizes[-1]
    should get the largest size as well.        
"""
def size_str_to_int(x):
    return float("inf") if x == 'original' else int(x[1:])

max_size = max(sizes, key=size_str_to_int)

IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}' 
r = requests.get(IMG_PATTERN.format(key=KEY,imdbid='tt0095016'))
api_response = r.json()

base_url = 'http://d3gtl9l2a4fn1j.cloudfront.net/t/p/'
max_size = 'original'
rel_path = 'mc7MubOLcIw3MDvnuQFrO9psfCa.jpg'
url = 'http://d3gtl9l2a4fn1j.cloudfront.net/t/p/original/mc7MubOLcIw3MDvnuQFrO9psfCa.jpg'

posters = api_response['posters']
poster_urls = []

for poster in posters:
    rel_path = poster['file_path']
    url = "{0}{1}{2}".format(base_url, max_size, rel_path)
    poster_urls.append(url)
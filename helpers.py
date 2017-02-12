import urllib.request
import urllib.parse
import json

def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)

def get_user_api_key():
    print('Enter your api key v3')
    user_api_key = input()
    try:
        make_tmdb_api_request(method='/movie/2', api_key=user_api_key)
    except urllib.error.HTTPError as err:
        if err.code == 401:
            print('Invalid api key')
            raise SystemExit
    else:
        return user_api_key

def get_movie_info(movie_number, user_api_key):
    film_info = make_tmdb_api_request(method='/movie/%d' % movie_number, api_key=user_api_key)
    return film_info

def get_movie_budget(movie_number, user_api_key):
    print(make_tmdb_api_request(method='/movie/%d' % movie_number, api_key=user_api_key)['budget'])
    
#=======================================================================================================
def load_data():
    print('Enter path to DataBase:')
    path = input()
    try:
        my_file = open(path, mode='r', encoding='utf-8')
        Films_data = json.load(my_file)
        return Films_data
    except FileNotFoundError:
        print('File not found, sorry...')
        raise SystemExit

def search_for_film(search, Films_data):
    films_founded = set()
    for film in Films_data:
        film_title = film['original_title'].split()
        if search in film_title:
            films_founded.add(film['original_title'])
    films_founded.remove(search)
    return films_founded

def is_there_my_film(search, Films_data):
    for film in Films_data:
        if search == film['original_title']:
            return film
    print('No such film in FilmsDB')
    raise SystemExit

def recommend_me_by(my_film, Films_data, by_this):
    films_founded = set()
    for film in Films_data:
        if film[by_this] == my_film[by_this]:
            films_founded.add(film['original_title'])
    films_founded.remove(my_film['original_title'])
    return films_founded


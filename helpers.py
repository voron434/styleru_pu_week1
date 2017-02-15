import urllib.request
import urllib.parse
import json
from getpass import getpass

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
    user_api_key = getpass()
    try:
        make_tmdb_api_request(method='/movie/2', api_key = user_api_key)
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

def save_films(user_api_key, num_of_films):
    big_data = []
    for film_id in range(num_of_films):
        try:
            big_data.append(get_movie_info(film_id, user_api_key))
            print('id: %s saved' % str(film_id))
        except urllib.error.HTTPError as err:
            if err.code == 404:  #if no film on this id
                print('id: %s is empty' % str(film_id))
                continue
            else:
                print('smth wrong with code...')
    return big_data

#=======================================================================================================
def load_data():
    print('Enter path to DataBase:')
    path = input()
    try:
        with open(path, mode='r', encoding='utf-8') as my_file:
            films_data = json.load(my_file)
            return films_data
    except FileNotFoundError:
        print('File not found, sorry...')
        raise SystemExit

def search_for_film(search, films_data):
    films_founded = set()
    for film in films_data:
        if search.lower() in film['original_title'].lower():
            films_founded.add(film['original_title'])
    return films_founded

def is_my_film_there(search, films_data):
    for film in films_data:
        if search == film['original_title']:
            return film
    print('No such film in FilmsDB')
    raise SystemExit

def recommend(my_film, films_data, num_to_recommend=8):
    params = {
        'belongs_to_collection': 1000,
        'original_language': 300,
        'budget': 100,
        'genres': 500
    }
    rating = {}
    for film in films_data:
        film_rate = 0
        for parameter in params:
            if film[parameter] == my_film[parameter]:
                film_rate += params[parameter]
        rating[film['original_title']] = film_rate

    films_founded = []
    for counter in range(num_to_recommend):
        max_rate = -1
        for film_title in rating:
            if rating[film_title] > max_rate:
                max_rate = rating[film_title]
                max_rated_film = film_title
        rating[max_rated_film] = -1
        films_founded.append(max_rated_film)
    return films_founded


import json
import urllib.request
import urllib.parse

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

def get_movie_info(movie_number):
    film_info = make_tmdb_api_request(method='/movie/' + str(movie_number), api_key=user_api_key)
    Film = {}
    Film[film_info['original_title']] = film_info #создаю словарик для фильма и выкидываю его через return
    return Film

def get_user_api_key():
    print('Enter your api key v3')
    user_api_key = input()
    try:
        make_tmdb_api_request(method='/movie/2', api_key = user_api_key)
    except urllib.error.HTTPError as err:
        if err.code == 401:
            print('invalid api key')
            raise SystemExit
    else:
        return user_api_key

user_api_key = get_user_api_key()
Big_Data = []
i = 0
film_number = 1

while i < 1000:
    try:
        Big_Data.append(get_movie_info(film_number)) #записываю в конец списка словарик из get_movie_info
        i += 1
        film_number += 1
    except urllib.error.HTTPError as err:
        if err.code == 404: #если на каком-то id нет фильма, то здесь это обработается
            print('id: ' + str(film_number) + ' is empty')
            film_number += 1
        else: #если ошибка не 404, то программа мне об этом скажет
            print('smth wrong with code...')

filename = 'MyFilmBD.json'
my_file = open(filename, mode='w', encoding='utf-8')
json.dump(Big_Data, my_file)
my_file.close()


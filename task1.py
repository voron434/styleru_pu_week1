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

def get_movie_budget(movie_number):
    print(make_tmdb_api_request(method='/movie/' + str(movie_number), api_key = user_api_key)['budget'])

def get_user_api_key():
    print('Enter your api key v3')
    user_api_key = input()
    try:
        make_tmdb_api_request(method='/movie/2', api_key = user_api_key)
    except urllib.error.HTTPError as err:
        if err.code == 401:
            print('Invalid api key')
            raise SystemExit
    else:
        return user_api_key

user_api_key = get_user_api_key()
get_movie_budget(215)

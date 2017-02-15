import json
import urllib.parse
from helpers import get_user_api_key
from helpers import get_movie_info

if __name__ == '__main__':
    user_api_key = get_user_api_key()
    big_data = []
    films_added = 0
    print('please, wait, this operation may take smth like 15-20 minutes')
    for film_id in range(2000):
        try:
            big_data.append(get_movie_info(film_id, user_api_key))
            films_added += 1
            print('films added: {}'.format(films_added))
        except urllib.error.HTTPError as err:
            if err.code == 404:  #if no film on this id
                continue
            else:
                print('smth wrong with code...')

    filename = 'MyFilmDB.json'
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json.dump(big_data, my_file)
        my_file.close()

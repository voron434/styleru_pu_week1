import json
import urllib.parse
from helpers import get_user_api_key
from helpers import get_movie_info

if __name__ == '__main__':
    user_api_key = get_user_api_key()
    Big_Data = []
    counter = 0
    film_number = 1
    print('please, wait, this operation may takesmth like 15-20 minutes')
    while counter < 1000:
        try:
            Big_Data.append(get_movie_info(film_number, user_api_key))
            counter += 1
            print('percent complete: {}'.format(counter/10))
            film_number += 1
        except urllib.error.HTTPError as err:
            if err.code == 404: #if no film on this id
                film_number += 1
            else:
                print('smth wrong with code...')

    filename = 'MyFilmDB.json'
    my_file = open(filename, mode='w', encoding='utf-8')
    json.dump(Big_Data, my_file)
    my_file.close()


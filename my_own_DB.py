import json
from helpers import get_user_api_key
from helpers import save_films

if __name__ == '__main__':
    user_api_key = get_user_api_key()
    films_amount = 1000
    print('please, wait, this operation may take smth like 15-20 minutes')
    big_data = save_films(user_api_key, films_amount)
    filename = 'MyFilmDB.json'
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json.dump(big_data, my_file)
        my_file.close()

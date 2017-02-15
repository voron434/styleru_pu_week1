from helpers import load_data
from helpers import search_for_film

if __name__ == '__main__':
    films_data = load_data()
    print('Enter film to search for:')
    search = input()
    result = search_for_film(search, films_data)
    for film in sorted(result):
        print(film)


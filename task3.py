from helpers import load_data
from helpers import search_for_film

if __name__ == '__main__':
    Films_data = load_data()
    print('Enter film to search for:')
    search = input().capitalize()
    search1 = search.lower()
    result = search_for_film(search1, Films_data)|search_for_film(search, Films_data)
    for film in sorted(result):
        print(film)

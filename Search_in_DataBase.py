from helpers import load_data
from helpers import search_for_film

if __name__ == '__main__':
    Films_data = load_data()
    print('Enter film to search for:')
    search = input()
    for film in sorted(search_for_film(search, Films_data)):
        print(film)

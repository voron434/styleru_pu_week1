from helpers import load_data
from helpers import search_for_film

if __name__ == '__main__':
    Films_data = load_data()
    print('Enter film to search for:')
    search = input()
    big_first = str(search[0]).capitalize() + search[1:len(search)]
    small_first = str(search[0]).lower() + search[1:len(search)]
    result = search_for_film(big_first, Films_data) or search_for_film(small_first, Films_data)
    for film in sorted(result):
        print(film)

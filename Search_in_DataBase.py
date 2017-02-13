from helpers import load_data
from helpers import search_for_film

if __name__ == '__main__':
    Films_data = load_data()
    print('Enter film to search for:')
    search = input()
    search1 = str(search[0]).capitalize() + search[1:len(search)]
    search2 = str(search[0]).lower() + search[1:len(search)]
    result = search_for_film(search1, Films_data) | search_for_film(search, Films_data)
    for film in sorted(result):
        print(film)

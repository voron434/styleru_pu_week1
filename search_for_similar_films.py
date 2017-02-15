from helpers import load_data
from helpers import is_my_film_there
from helpers import recommend

if __name__ == '__main__':
    films_data = load_data()
    print('Enter film to search for:')
    search = input()
    my_film = is_my_film_there(search, films_data)
    recommendation = recommend(my_film, films_data)

    for film in sorted(recommendation):
        print(film)



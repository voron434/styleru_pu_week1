from helpers import load_data
from helpers import is_there_my_film
from helpers import search_for_film
from helpers import recommend_me_by

if __name__ == '__main__':
    Films_data = load_data()
    print('Enter film to search for:')
    search = input()
    my_film = is_there_my_film(search, Films_data)
    recommend = search_for_film(search, Films_data)
    num_of_films_to_recommend = 8

    if len(recommend) < num_of_films_to_recommend:
        recommend_by_budget = recommend_me_by(my_film, Films_data, 'budget')
        while len(recommend_by_budget)>num_of_films_to_recommend-len(recommend):
            recommend_by_budget.pop()

    for film in sorted(recommend):
        print(film)
    for film in sorted(recommend_by_budget):
        print(film)

from helpers import load_data
from helpers import is_my_film_there
from helpers import search_for_film
from helpers import recommend_me_by

if __name__ == '__main__':
    films_data = load_data()
    print('Enter film to search for:')
    search = input()
    my_film = is_my_film_there(search, films_data)
    recommendation = search_for_film(search, films_data)
    recommendation.remove(search)
    num_of_films_to_recommend = 8

    if len(recommendation) < num_of_films_to_recommend:
        recommendion_by_budget = recommend_me_by(my_film, films_data, 'budget')
        for film in range(len(num_of_films_to_recommend - len(recommendation))):
            recommendation_by_budget.pop()

    for film in sorted(recommendation):
        print(film)
    for film in sorted(recommendation_by_budget):
        print(film)


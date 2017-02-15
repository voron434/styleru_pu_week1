from helpers import get_user_api_key
from helpers import get_movie_budget

if __name__ == '__main__':
    user_api_key = get_user_api_key()
    get_movie_budget(215, user_api_key)


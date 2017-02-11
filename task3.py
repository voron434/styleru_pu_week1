import json

def search_for_film(search):
    for film in Films_data:
        for elem in film:
            if search in elem:
                results.append(elem)

def load_data():
    print('Enter path to DataBase:')
    path = input()
    try:
        my_file = open(path, mode='r', encoding='utf-8')
        Films_data = json.load(my_file)
        return Films_data
    except FileNotFoundError:
        print('File not found, sorry...')
        raise SystemExit

Films_data = load_data()

print('Enter film to search for:')
search = input().capitalize()
search1 = search.lower()

results = []

search_for_film(search)
search_for_film(search1)

for film in sorted(results):
    print(film)

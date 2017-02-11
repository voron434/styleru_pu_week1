import json

def is_there_my_film(search):
    result = ''
    for num, film in enumerate(Films_data):
        for elem in film:
            if search == elem:
                result = elem
                my_film_num = num
    if result == '':
        print('No such film in DataBase!!!')
        raise SystemExit
    return result, my_film_num

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
print('Enter some film to find similar films:')
my_film, my_film_num = is_there_my_film(input())
#---------------Search------------------
recommend = set()
for film in Films_data:
    for name in film:
        for word in name.split():
            if word in my_film.split():
                recommend.add(name)
if len(recommend) < 8:
    for film in Films_data:
        for name in film:
            if film[name]['budget'] == Films_data[my_film_num][my_film]['budget']:
                recommend.add(name)
recommend.remove(my_film)
if len(recommend) == 0:
    print('Sorry, no any similar films in DataBase')
for elem in sorted(recommend):
    print(elem)

import random

shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал',
         '24': 'драма', 'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}

ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}

film = {}
for k, v in shows.items():
    if v != 'фэнтази':
        film.setdefault(k)

for k,v in film.items():
    film[k] = ratings.get(k,v)

films = [k for k, v in film.items() if v >= 0.85]

zz = random.choice(films)
while True:
    user = input(f'Нравиться вам фильм "{zz}" [y/n]?')
    if user != 'y':
        zz = random.choice(films)
    else:
        print(f'Вы выбрали фильм "{zz}" приятного просмотра')
        break

import re

animals = ['питон', 'питон', 'кит', 'собака', 'питон', 'кит', 'кошка', 'горилла', 'кит', 'кошка', 'жираф', 'леопард',
           'жираф', 'жираф', 'кошка', 'горилла', 'жираф', 'жираф', 'кошка', 'жираф', 'кошка', 'кошка', 'собака', 'кит',
           'жираф', 'леопард', 'жираф', 'собака', 'кит', 'кит', 'кит', 'жираф', 'собака', 'собака', 'кит', 'питон',
           'леопард', 'кошка', 'жираф', 'собака', 'кошка', 'жираф', 'кошка', 'собака', 'кит', 'леопард', 'леопард',
           'горилла', 'горилла', 'кит']

# Выоборка с помощью filter название начинается с к
spisok1 = list(filter(lambda n: re.match('к[а-я]+', n), animals))
print(spisok1)

# Выоборка с помощью filter название начинается с л
spisok2 = list(filter(lambda n: re.match('л[а-я]+', n), animals))
print(spisok2)


# Выоборка с помощью list comprehension название начинается с л
spisok_л = [n for n in animals if re.match('л[а-я]+', n)]
print(spisok_л)

# Выоборка с помощью list comprehension название начинается с к
spisok_к = [n for n in animals if re.match('к[а-я]+', n)]
print(spisok_к)
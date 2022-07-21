"""В нашей школе мы не можем разглашать персональные данные пользователей, но
чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют в
виду (у преподавателей, например, часто учится несколько Саш), мы генерируем
пользователям уникальные и легко произносимые имена. Имя у нас состоит из
прилагательного, имени животного и двузначной цифры. В итоге получается,
например, "Перламутровый лосось 77". Для генерации таких имен мы и решали
следующую задачу:
Получить с русской википедии список всех животных (https://inlnk.ru/jElywR) и
вывести количество животных на каждую букву алфавита. Результат должен
получиться в следующем виде:

А: 642
Б: 412
В:....
"""

# Для сбора данных с сайта использовался фреймворк Scrapy.
from pprint import pprint
from collections import Counter


animals_from_file = []
with open('animals/animals.txt', 'r', encoding='UTF-8') as file:
    animals_line = file.readline()
    animals_from_file.append(animals_line)

animals_list = animals_from_file[0].split(',')
result = []
for animal in animals_list:
    result.append(animal[2])

cnt = Counter(result)
pprint(dict(cnt))

"""Когда пользователь заходит на страницу урока, мы сохраняем время его захода.
Когда пользователь выходит с урока (или закрывает вкладку, браузер – в общем
как-то разрывает соединение с сервером), мы фиксируем время выхода с урока.
Время присутствия каждого пользователя на уроке хранится у нас в виде
интервалов. В функцию передается словарь, содержащий три списка с таймстемпами
(время в секундах):

lesson – начало и конец урока
pupil – интервалы присутствия ученика
tutor – интервалы присутствия учителя
Интервалы устроены следующим образом – это всегда список из четного количества
элементов. Под четными индексами (начиная с 0) время входа на урок, под
нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и
возвращает время общего присутствия ученика и учителя на уроке (в секундах).
"""


def appearance(intervals) -> int:
    """Получить количество общего времени для lesson, pupil и tutor"""
    global_list = []

    lesson = intervals['lesson']
    lesson_common = []
    lesson_list_of_ranges = list_append_numbers(lesson)
    for les in lesson_list_of_ranges:
        lesson_common.extend(les)
    global_list.append(lesson_common)

    pupil = intervals['pupil']
    pupil_common = []
    pupil_list_of_ranges = list_append_numbers(pupil)
    for pup in pupil_list_of_ranges:
        pupil_common.extend(pup)
    global_list.append(pupil_common)

    tutor = intervals['tutor']
    tutor_common = []
    tutor_list_of_ranges = list_append_numbers(tutor)
    for tut in tutor_list_of_ranges:
        tutor_common.extend(tut)
    global_list.append(tutor_common)

    # Получение общих значений времени для lesson, pupil и tutor в
    # интервалах секунд
    general_result = set.intersection(*map(set, global_list))

    # Получение общего количества секунд одновременного присутствия
    return len(sorted(general_result))


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


def list_append_numbers(array) -> list:
    """Получить списки интервалов в секундах """
    first_index = 1
    result = []
    for ind in array:
        if array.index(ind) % 2 == 0:
            first_index = ind
        else:
            result.append([num for num in range(first_index, ind + 1)])

    return result

# Логика работает, но выходные данные отличаются от представленных ответов
# 2-4 секунды
if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

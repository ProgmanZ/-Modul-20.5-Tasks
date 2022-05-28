# Задача 1. Паспортные данные

def check_data(user_tuple):
    for item in user_tuple:
        if item.isalpha():
            return False
    return True


data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

user_string = (int(element) for element in input('Введите серию и номер паспорта через пробел: ').strip().split(' ')
               if check_data(element))

user_string = tuple(user_string)

print('{0} {1}'.format(data[user_string][0], data[user_string][1]) if user_string in data else 'Таких в БД нет')
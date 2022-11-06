#комментарий

number: int = 42
#print(type(number))

it_is_a_list: bool = True

value: object = [1, 2, 3, 8] if it_is_a_list else number

#print(value)

text = "its a string"

multi_line_text = '''
line 1
line 2
line 3
'''
print(multi_line_text)

def user_info(name, age, city):
    """Возвращает информацию о пользователе

    :param name: имя
    :param age: возраст в годах
    :param city: город
    """
    return name + ' ' + age + ', ' + city
#переменные
a = 1
b = 'hello'
#print(b.upper())

#Пустой тип
var = None

#Булевый тип
isCat: bool = True
isDog = False

# Числа
a: int = -1
b: float = 19.39487538475
c: complex = 19 + 12j
print(c.imag, c.real)

d = a + b

from decimal import Decimal, getcontext
getcontext().prec = 5
value = Decimal(0.0)

for _ in range(100):
    value += Decimal(0.2)
print(value)

#print(5 ** 1_000)

#Деление целых чисел
print(9 / 7)
print(9 // 7)
print(9 % 7)

bin_var = 0b101
#oct_var = 0866
hex_var = 0xff

#Строки
string: str = 'just a string'
print(string)

raw_string = r"line_1\nline2\nline3"
#print(raw_string)

#Списки

numbers: list = [1, 2, 3, 5, 6]
users = ['Alice', 'Bob', 'Carlos']
things = [1, True, 'Text', None,[1, 2, 3]]

numbers += [34, 35, 35]
print(users)
print(len(numbers))
print(numbers[2])
#последний элемент
print(numbers[-1])
#срез, слайс
print(numbers[1:3], numbers[2:-2])

#Кортежи
location = (56.3455, 84.234234, "Tomsk")
print(location[1])

#Распаковка кортежа
latitude, longitude, label = location
assert latitude == 56.3455
assert longitude == 84.234234
assert label == 'Tomsk'

#Словари
location = {
    'latitude': 56.3455,
    'longitude': 84.234234,
    'label': 'Tomsk',
}

location['latitude'] == 56.3455
location['population'] = 500_000

del location['label']
print(location)

locations = {
    'Tomsk': (345345, 34534),
    'Kazan': (1, 1),
    'Moscow': (2,2)
}

print(locations['Tomsk'])

d = {
    1: "one",
    4: "four",
}
print(d[1])


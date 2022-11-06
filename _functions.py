from math import *
def print_sqr(value: int, label: str):
    print(value * value, label)

for x in [1, 201, 3, 7, 4, 5]:
    print_sqr(x, "***")

def _sum(a, b):
    return a + b


res = _sum(2, 9)
res2 = _sum("Hello, ", "world")
print(res, res2)


def f(x:  float) -> float:
    return _sum(3, x) * exp(10) + sin(34)

#вычисляет числа Фиббаначи
def _fib(max_value: int):
    a, b = 0, 1

    while a <= max_value:
        print(a)
        a, b = b, a + b

_fib(2000)

#Функция-генератор. Может сохранять свое состояние между вызовами
def _fib_gen():
    a, b = 0, 1

    #вот тут вернем и выйдем из ф-ии
    yield a

    # При повтором вызове вызовем отсюда
    yield b

    while True:
        a, b = b, a + b
        yield b

if __name__ == '__main__':
    #Л-функция (безым ф-ия, кот может использоваться на месте)
    _f = lambda x: _sum(3, x) * exp(10) + sin(34)
    assert f(23.09) == _f(23.09)

    gen = _fib_gen()
    print(next(gen))
    print(next(gen))
    print(next(gen))


# import time
#
# for n in gen:
#      time.sleep(1)
#      print(n)

names = ['Alice', 'Bob', 'Carlos', 'David', 'Eva']
transformed_names = []
for name in names:
    transformed_names.append(name)
print(names)
print(transformed_names)

# Генератор списка (Не путать с генераторами!). Пишем код наполнения списка прямо внутри [].
transformed_names = [name.upper() for name in names if len(name) > 3]
print(transformed_names)

# А это генератор. Очень похоже на список выше, но полученная коллекция вычисляется по мере итерации по ней.
transformed_names = [name.upper() for name in names if len(name) > 3]
for n in transformed_names:
    print(n)


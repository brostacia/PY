#ПОЛЬЗОВАТЕЛЬСКИЕ ТИПЫ
from enum import Enum
from dataclasses import dataclass

#тип Перечесление (enum)
class DefaultColor(Enum):
    Red = (255, 0, 0),
    Green = (0, 255, 0),
    Blue = (0, 0, 255),
    Black = (255, 255, 255),
    White = (0, 0, 0),

color: DefaultColor = DefaultColor.Red
print(color)
print(color.name, color.value)

#Класс данных
@dataclass
class Location:
    latitude: float
    longitude: float
    label: str

location = Location(56.45345, 84.2343, 'Tomsk')
print(location)

assert location.latitude == 56.45345

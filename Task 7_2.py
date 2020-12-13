"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from math import ceil
from abc import ABC, abstractmethod

class Clothes(ABC):
     def __init__(self, arg):
         self.arg = arg

     @abstractmethod
     def calculation(self):
         pass

class Coat(Clothes):
     @property
     def calculation(self):
         return ceil(self.arg / 6.5 + 0.5)

class Costume(Clothes):
     @property
     def calculation(self):
         return ceil(2 * self.arg + 0.3)

coat = Coat(46)
costume = Costume(188)

print(coat.calculation)
print(costume.calculation)
from enum import Enum


class State(Enum):
    START = 0
    MAIN = 1
    TOURNAMENTS = 2
    SOCCER = 3
    HAT = 4
    POKER = 5
    PIZZA = 6
    SALAD = 7
    SNACK = 8
    DRINK = 9
    DESSERT = 10
    PIZZA1 = 11
    PIZZA2 = 12
    PIZZA3 = 13
    PIZZA4 = 14
    PIZZA5 = 15
    BAG = 16
    ORDER = 17
    ORDER2 = 18

    @staticmethod
    def from_int(value: int):
        if value not in State._value2member_map_:
            raise ValueError("Not value of enum 'State'")
        return State._value2member_map_[value]
from enum import Enum


class AccessLevel(Enum):
    UNAUTHORIZED = 1
    READ = 2
    WRITE = 3
    PREP = 4
    SUPERUSER = 5

    @staticmethod
    def from_int(value: int) -> 'AccessLevel':
        if value not in AccessLevel._value2member_map_:
            raise ValueError("Not value of enum 'AccessLevel'")
        return AccessLevel._value2member_map_[value]

    @staticmethod
    def from_string(value: str) -> 'AccessLevel':
        value = value.split('.')[-1]
        if value not in AccessLevel._member_map_:
            raise ValueError("Not value of enum 'AccessLevel'")
        return AccessLevel._member_map_[value]

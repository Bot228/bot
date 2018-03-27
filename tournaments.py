from enum import Enum
from typing import Callable, Union


class ButtonType(Enum):
    Hat = (u'\U0001F3A9', 'Помощник библиотекаря')
    Back = (u'\U00002B05', 'Назад')
    Poker = ('🍛 Меню в столовой')
    Soccer = ('📜', 'Расписание уроков')
    Pizza = ('☎ Контакты')
    Salad = ('⏰ Расписание звонков')
    Bag = ('📝 График дежурств')
    Pizza_info_no = (u'\U00002B05', 'Назад')
    @staticmethod
    def from_string(value: str):
        for name in ButtonType._member_names_:
            member = ButtonType._member_map_[name]
            if str(member) == value:
                return member
        raise ValueError("Not value of enum 'Smile'")

    def __str__(self):
        return "{} {}".format(self.value[0], self.value[1])



class TournamentInfo:
    def __init__(self, has_team_name: bool, team_size: int, check_additional_info: Union[Callable, None]):
        self.has_team_name = has_team_name
        self.team_size = team_size
        self.check_additional_info = check_additional_info


def check_hat_info(info: str):
    return len(info.split()) == 20

soccer_info = TournamentInfo(has_team_name=True, team_size=6, check_additional_info=None)
hat_info = TournamentInfo(has_team_name=False, team_size=2, check_additional_info=check_hat_info)
poker_info = TournamentInfo(has_team_name=False, team_size=1, check_additional_info=None)


from typing import Union, Iterable

from telebot import logger
from persistent_storage1.file_storage import JsonFileStorage
from states import State


class UserInfo:
    def __init__(self,
                 user_id: int,
                 state: State):
        self.user_id = user_id
        self.state = state

    def __str__(self):
        return "User id: {}\nUser name: {}\nName: {}\nAccess_level: {}".format(
            self.user_id, self.nickname, self.name, self.access_level
        )


class UsersRepository:
    def __init__(self, path: str):
        self._storage = JsonFileStorage(path)

    def save(self, info: UserInfo):
        key = str(info.user_id)
        self._storage.write(key, {"state": info.state.value})

    def read(self, user_id: int) -> UserInfo:
        if not self.exists(user_id):
            logger.error("User %s does not exist", user_id)
            raise KeyError('User does not exist')
        info = self._storage.read(str(user_id))
        # noinspection PyTypeChecker
        return UsersRepository._to_user_info(info, user_id)

    @staticmethod
    def _to_user_info(info: dict, user_id: int) -> UserInfo:
        state = State.from_int(info["state"])
        return UserInfo(user_id, state)

    def exists(self, user_id: int) -> bool:
        try:
            self._storage.read(str(user_id))
        except FileNotFoundError:
            return False
        else:
            return True

    def change_state(self, user_id: int, state: State):
        info = self.read(user_id)
        info.state = state
        self.save(info)

    def update_nickname(self, user_id: int, nickname: str):
        info = self.read(user_id)
        if info.nickname != nickname:
            info.nickname = nickname
            self.save(info)

    def find_user_by_nickname(self, nickname) -> Union[UserInfo, None]:
        for info in self.read_all():
            if info.nickname == nickname:
                return info
        return None

    def read_all(self) -> Iterable[UserInfo]:
        for file_id in self._storage.read_all():
            user_id = int(file_id)
            yield self.read(user_id)

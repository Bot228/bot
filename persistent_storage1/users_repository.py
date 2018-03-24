from persistent_storage1.file_storage import JsonFileStorage
from states import State


class UsersRepository:
    def __init__(self, path: str):
        self._storage = JsonFileStorage(path)

    def save(self, user_id: int, state: State):
        key = str(user_id)
        self._storage.write(key, {"state": state.value})

    def read(self, user_id: int) -> State:
        if not self.exists(user_id):
            raise KeyError("User does not exist")
        key = str(user_id)
        return State.from_int(self._storage.read(key)["state"])

    def exists(self, user_id: int) -> bool:
        try:
            self._storage.read(str(user_id))
        except FileNotFoundError:
            return False
        else:
            return True
import json

import os
from typing import Iterable


class RawFileStorage:

    def __init__(self, path: str):
        self.path = path

    def write(self, file_id: str, data: str) -> None:
        with open(file=self._get_file_path(file_id), mode='wb') as file:
            file.write(bytes(data, encoding='utf-8'))

    def read(self, file_id: str) -> str:
        with open(file=self._get_file_path(file_id), mode='rb') as file:
            return str(file.read(), encoding='utf-8')

    def delete(self, file_id: str):
        os.remove(self._get_file_path(file_id))

    def _get_file_path(self, file_id: str):
        file_path = '/'.join([self.path, file_id])
        return file_path

    def read_all(self) -> Iterable[str]:
        for file_id in os.listdir(self.path):
            if file_id.startswith('.'):
                continue
            yield file_id


class JsonFileStorage(RawFileStorage):
    def write(self, file_id: str, data: object) -> None:
        super().write(file_id, json.dumps(data, ensure_ascii=False, indent=2))

    def read(self, file_id: str) -> object:
        return json.loads(super().read(file_id))

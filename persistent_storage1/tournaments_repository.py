from datetime import datetime
from typing import List
import uuid

import time

import helpers
from persistent_storage.file_storage import JsonFileStorage
from states import State


class TournamentData:
    def __init__(self, team_name: str, members: List[str], additional_text: str):
        self.team_id = str(uuid.uuid4())
        self.timestamp = int(datetime.utcnow().timestamp())
        self.team_name = team_name
        self.members = members
        self.additional_text = additional_text


class TournamentsRepository:
    def __init__(self, path):
        self._storage = JsonFileStorage(path)

    def save(self, user_id: int, tournament_type: State, data: TournamentData) -> None:
        if not helpers.is_concrete_tournament(tournament_type):
            raise ValueError("State is not concrete tournament")
        file_id = "{}.txt".format(tournament_type.name)
        tournament = self._safe_read_json(file_id)
        tournament.append({
            "team_id": data.team_id,
            "user_id": user_id,
            "timestamp": data.timestamp,
            "team_name": data.team_name,
            "members": data.members,
            "additional_text" : data.additional_text,
        })
        self._storage.write(file_id, tournament)

    def _safe_read_json(self, file_id: str) -> List:
        try:
            return list(self._storage.read(file_id))
        except FileNotFoundError:
            return []

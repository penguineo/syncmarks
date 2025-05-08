from typing import List


class Browser:
    def __init__(self, name: str) -> None:
        self.name = name

    def is_installed(self) -> bool:
        raise NotImplementedError

    def get_bookmarks(self, profiles: List[str]) -> list[dict]:
        raise NotImplementedError

    def extract_bookmarks(self, data: dict) -> list[dict]:
        raise NotImplementedError

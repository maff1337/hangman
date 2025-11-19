from typing import Any
from pathlib import Path
from tomllib import load as toml_load


class Config:
    _config: dict[str, Any]

    def __init__(self, path: Path) -> None:
        self._config = self._load(path)

    def _load(self, path: Path) -> dict[str, Any]:
        with open(path, mode='rb') as file:
            return toml_load(file)

    def __getitem__(self, key: str) -> Any:
        return self._config[key]

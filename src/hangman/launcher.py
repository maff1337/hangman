from pathlib import Path

from hangman.configs.config import Config
from hangman.domain.game_handler import GameHandler


def main() -> None:
    path = Path(__file__).parent / 'config.toml'
    config = Config(path)

    game = GameHandler(config)

    game.main_menu()

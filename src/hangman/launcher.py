from pathlib import Path

from hangman.config import Config
from hangman.game_handler import GameHandler


def main() -> None:
    path = Path(__file__).parent / 'config.toml'
    config = Config(path)

    game = GameHandler(config)

    game.main_menu()

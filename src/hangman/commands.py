from enum import Enum


class MainMenuCommands(Enum):
    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    FOURTH = '4'


class LanguageCommands:
    language = {
        '1': 'ru',
        '2': 'en'
    }

    @classmethod
    def get_language(cls, choice: str) -> str | None:
        return cls.language.get(choice, None)


class DifficultyCommands:
    dufficulty = {
        '1': 'easy',
        '2': 'medium',
        '3': 'hard'
    }

    @classmethod
    def get_difficulty(cls, choice: str) -> str | None:
        return cls.dufficulty.get(choice, None)

from pathlib import Path
from tomllib import load as toml_load
from random import choice as random_choice

from hangman.configs.config import Config
from hangman.presentation.renderer import Renderer
from hangman.domain.validator import Validator
from hangman.domain.word_hander import WordHandler
from hangman.domain.exceptions import ValidationException
from hangman.domain.commands import DifficultyCommands, LanguageCommands, MainMenuCommands


class GameHandler:
    def __init__(self, config: Config) -> None:
        self._config = config

        self._language = self._config['game']['default_language']
        self._difficulty = self._config['game']['default_difficulty']

        self._mask_char = self._config['game']['mask_char']
        self._max_mistakes = self._config['game']['max_mistakes']
        self._load_words()

        self.validator = Validator(
            self._config['game']['alphabets'][self._language])

        self.renderer = Renderer()
        self._update_locale(self._language)

    def _load_words(self) -> None:
        glossary_path = Path(
            self._config['difficulty'][self._language][self._difficulty])

        with open(glossary_path, 'r', encoding='utf-8') as f:
            self._words = list(map(lambda x: x.strip(), f.readlines()))

    def _update_locale(self, locale: str) -> None:
        locale_path = Path(self._config['locale'][locale])

        with open(locale_path, 'rb') as f:
            self.renderer.update_phrases(toml_load(f))

            self.validator.update_alphabet(
                self._config['game']['alphabets'][locale])

            self._load_words()

    def select_language(self) -> None:
        while True:
            self.renderer.print_language_prompt()
            choice = input()

            language = LanguageCommands.get_language(choice)
            if language:
                self._language = language
                self._update_locale(self._language)
                break
            else:
                self.renderer.print_invalid_choice()

    def select_difficulty(self) -> None:
        while True:
            self.renderer.print_difficulty_prompt()
            choice = input()

            difficulty = DifficultyCommands.get_difficulty(choice)
            if difficulty:
                self._difficulty = difficulty
                self._load_words()
                break
            else:
                self.renderer.print_invalid_choice()

    def main_menu(self) -> None:
        self.renderer.print_main_menu()
        while True:
            self.renderer.print_current_status(
                self._language, self._difficulty)

            self.renderer.print_main_menu_prompt()
            self.renderer.print_main_menu_options()

            choice = input()

            match choice:
                case MainMenuCommands.FIRST.value:
                    self.start_game()
                case MainMenuCommands.SECOND.value:
                    self.select_difficulty()
                case MainMenuCommands.THIRD.value:
                    self.select_language()
                case MainMenuCommands.FOURTH.value:
                    self.renderer.print_goodbye()
                    break
                case _:
                    self.renderer.print_invalid_choice()

    def still_play(self, mistakes: int, mask: list[str]) -> bool:
        return mistakes <= self._max_mistakes and self._mask_char in mask

    def is_lost(self, mistakes: int) -> bool:
        return mistakes > self._max_mistakes

    def start_game(self) -> None:
        word_handler = WordHandler(
            word=random_choice(self._words),
            mask_char=self._mask_char
        )

        mistakes = 0
        used_letters = list()

        while self.still_play(mistakes, word_handler.mask):
            letter: str

            while True:
                self.renderer.print_current_game_state(
                    mistakes,
                    self._max_mistakes,
                    word_handler.mask,
                    used_letters
                )

                letter = input().lower()

                try:
                    self.validator.validate(letter, used_letters)
                except ValidationException as e:
                    self.renderer.print_error_message(e.config_name)
                    continue

                break

            used_letters.append(letter)

            if word_handler.is_word_contains(letter):
                word_handler.reveal_letter(letter)
            else:
                mistakes += 1

        if self.is_lost(mistakes):
            self.renderer.print_lost_result(mistakes, word_handler.word)
        else:
            self.renderer.print_won_result(word_handler.word)

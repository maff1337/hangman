from typing import Any

from hangman.presentation.gallows import Gallows
from hangman.domain.word_hander import Word


class Renderer:
    def __init__(self) -> None:
        self._phrases = dict()
        self.gallows = Gallows

    def update_phrases(self, new_phrases: dict[str, Any]) -> None:
        self._phrases = new_phrases

    def print_error_message(self, name: str) -> None:
        print(self._phrases['error_messages'][name])

    def print_main_menu(self) -> None:
        print(self._phrases['menu']['main']['welcome'])

    def print_current_status(self, locale: str, difficulty: str) -> None:
        language = self._phrases['menu']['language'][locale]
        hdifficulty = self._phrases['menu']['difficulty'][difficulty]

        current_status = self._phrases['menu']['main']['current_status']
        print(current_status.format(language=language, difficulty=hdifficulty))

    def print_main_menu_prompt(self) -> None:
        print(self._phrases['menu']['main']['prompt'])

    def print_main_menu_options(self) -> None:
        print(self._phrases['menu']['main']['menu_options'])

    def print_goodbye(self) -> None:
        print(self._phrases['menu']['main']['goodbye'])

    def print_language_prompt(self) -> None:
        ru = self._phrases['menu']['language']['ru']
        en = self._phrases['menu']['language']['en']

        prompt = self._phrases['menu']['language']['prompt']
        print(prompt.format(ru=ru, en=en))

    def print_difficulty_prompt(self) -> None:
        easy = self._phrases['menu']['difficulty']['easy']
        medium = self._phrases['menu']['difficulty']['medium']
        hard = self._phrases['menu']['difficulty']['hard']

        prompt = self._phrases['menu']['difficulty']['prompt']
        print(prompt.format(easy=easy, medium=medium, hard=hard))

    def print_invalid_choice(self) -> None:
        print(self._phrases['menu']['common']['invalid_choice'])

    def print_current_game_state(
        self,
        mistakes: int,
        max_mistakes: int,
        mask: list[str],
        used: list[str]
    ) -> None:
        print(self.gallows.get_stage(mistakes))
        print(' '.join(mask), '\n')
        print(self._phrases['gameplay']['used_letters'], ', '.join(used))

        mistakes_info = self._phrases['gameplay']['mistakes_info']

        print(mistakes_info.format(mistakes=mistakes, max_mistakes=max_mistakes))
        print(self._phrases['gameplay']['request_letter'])

    def print_lost_result(self, mistakes: int, word: Word) -> None:
        print(self.gallows.get_stage(mistakes))
        print(self._phrases['results']['lost'])
        print(self._phrases['results']['word_was'].format(word=word))

    def print_won_result(self, word: Word) -> None:
        print(self._phrases['results']['won'])
        print(self._phrases['results']['word_was'].format(word=word))

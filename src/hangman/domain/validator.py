from hangman.domain.exceptions import AlphabetMismatchError, AlreadyUsedLetterError, SingleLetterRequiredError


class Validator:
    def __init__(self, alphabet: str) -> None:
        self._alphabet = alphabet

    def _is_single_letter(self, letter: str) -> bool:
        return len(letter) == 1

    def _is_correct_alphabet(self, letter: str) -> bool:
        return letter in self._alphabet

    def _is_letter_already_used(self, letter: str, used: list[str]) -> bool:
        return letter in used

    def update_alphabet(self, alphabet: str) -> None:
        self._alphabet = alphabet

    def validate(self, letter: str, used: list[str]) -> None:
        if not self._is_single_letter(letter):
            raise SingleLetterRequiredError()

        if not self._is_correct_alphabet(letter):
            raise AlphabetMismatchError()

        if self._is_letter_already_used(letter, used):
            raise AlreadyUsedLetterError()

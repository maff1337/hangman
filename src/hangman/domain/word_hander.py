type Word = str


class WordHandler:
    _word: Word
    _mask: list[str]

    mask_char: str

    def __init__(self, word: Word, mask_char: str) -> None:
        self._word = word
        self._mask = [mask_char] * len(word)

        self.mask_char = mask_char

    @property
    def mask(self) -> list[str]:
        return self._mask

    @property
    def word(self) -> str:
        return self._word

    def is_word_contains(self, letter: str) -> bool:
        return letter in self._word

    def reveal_letter(self, letter: str) -> None:
        for idx, character in enumerate(self._word):
            if letter == character:
                self._mask[idx] = letter

class ValidationException(Exception):
    config_name: str


class SingleLetterRequiredError(ValidationException):
    config_name = 'single_required'

    def __init__(self) -> None:
        super().__init__('Input must be a single letter')


class AlphabetMismatchError(ValidationException):
    config_name = 'alphabet_mismatch'

    def __init__(self) -> None:
        super().__init__('Input letter does not belong to the expected alphabet')


class AlreadyUsedLetterError(ValidationException):
    config_name = 'already_used'

    def __init__(self) -> None:
        super().__init__('Input letter has already been used')

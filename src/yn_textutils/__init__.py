import string

import rich

_TABLE = str.maketrans("", "", string.punctuation)


def remove_punctuation(text: str) -> str:
    return text.translate(_TABLE)


def as_words(text: str) -> list[str]:
    return remove_punctuation(text).casefold().split()


def main() -> None:
    import sys

    rich.print(as_words(sys.argv[1]))

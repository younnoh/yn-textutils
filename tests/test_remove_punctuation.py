import pytest

from yn_textutils import remove_punctuation

@pytest.mark.parametrize(
    ["text", "expected"],
    [
        ("that's", "thats"),
        ("depth-first", "depthfirst"),
        ("DB_HOST", "DBHOST"),
    ],
)
def test_removes_internal_punctuation(text, expected):
    assert remove_punctuation(text) == expected

@pytest.mark.parametrize(
    ["text", "expected"],
    [
        ("*special", "special"),
        ("@Rodrigo", "Rodrigo"),
    ],
)
def test_removes_leading_punctuation(text, expected):
    assert remove_punctuation(text) == expected
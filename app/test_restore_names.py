import pytest
from app.restore_names import restore_names


def test_restore_only_missing_names() -> None:
    assert restore_names(
        [
            {
                "last_name": "Holy",
                "full_name": "Martin Holy",
            }
        ]
    ) == (
        [
            {
                "first_name": "Martin",
                "last_name": "Holy",
                "full_name": "Martin Holy",
            }
        ]
    )


def test_restore_only_none_names() -> None:
    assert restore_names(
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Holy",
            }
        ]
    ) == (
        [
            {
                "first_name": "Mask",
                "last_name": "Holy",
                "full_name": "Mask Holy",
            }
        ]
    )

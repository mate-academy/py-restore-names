import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "failed_db, restored_db",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
        )
    ],
)
def test_is_restore_correct(failed_db: list, restored_db: list) -> None:
    restore_names(failed_db)
    assert failed_db == restored_db

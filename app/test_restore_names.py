import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user,first_name",
    [
        (
            {"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            "Jack",
        ),
        (
            {"last_name": "Adams",
             "full_name": "Mike Adams"},
            "Mike",
        ),
        (
            {"last_name": "Tumberg",
                "full_name": "Gretta Tumberg"},
            "Gretta",
        )
    ]
)
def test_restored_names(
        user: dict,
        first_name: str
) -> None:
    restore_names([user])
    assert user["first_name"] == first_name

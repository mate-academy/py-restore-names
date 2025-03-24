import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": None,
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ]
        ),
    ]
)
def test_should_set_first_name_if_none(users: list[dict]) -> None:
    restore_names(users)

    for user in users:
        assert user["first_name"] is not None


@pytest.mark.parametrize(
    "users",
    [
        (
            [
                {
                    "last_name": "Jam",
                    "full_name": "Sam Jam",
                },
                {
                    "last_name": "Rem",
                    "full_name": "Dean Rem",
                },
            ]
        ),
    ]
)
def test_should_define_first_name_and_set(users: list[dict]) -> None:
    restore_names(users)

    for user in users:
        assert "first_name" in user

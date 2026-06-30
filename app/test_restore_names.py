import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        pytest.param(
            [
                {
                    "first_name": "",
                    "full_name": "Sam Black"
                }
            ],
            [
                {
                    "first_name": "Sam",
                    "full_name": "Sam Black"
                }
            ],
            id="test 'first name' is empty string"
        ),
        pytest.param(
            [
                {
                    "first_name": None,
                    "full_name": "Samuel Jackson"
                }
            ],
            [
                {
                    "first_name": "Samuel",
                    "full_name": "Samuel Jackson"
                }
            ],
            id="test 'first name' is None"
        ),
        pytest.param(
            [
                {
                    "full_name": "Rose White",
                }
            ],
            [
                {
                    "first_name": "Rose",
                    "full_name": "Rose White",
                }
            ],
            id="test no 'first name' field"
        )
    ]
)
def test_restores_names_correctly(
    users: list[dict],
    expected: list[dict]
) -> None:
    restore_names(users)
    assert users == expected


@pytest.mark.parametrize(
    "users, expected_exception",
    [
        pytest.param(
            [{}], KeyError,
            id="test empty dict"
        ),
        pytest.param(
            [
                {
                    "first_name": "Sam",
                    "full_name": "Sam Smith"
                },
                {
                    "first_name": "Nancy",
                    "full_name": None
                }
            ],
            KeyError,
            id="test user`s 'full_name' is None"
        ),
        pytest.param(
            [
                {
                    "first_name": "Nastya"
                },
                {
                    "first_name": "Alex",
                    "last_name": "Black"
                }
            ],
            KeyError,
            id="test user has no 'full name' field"
        ),
        pytest.param(
            [
                {
                    "last_name": "Doe",
                    "full_name": "123-- Doe"
                }
            ],
            ValueError,
            id="test user`s full_name has numbers or special symbols"

        ),
        pytest.param(
            [
                {
                    "first_name": "00000",
                    "full_name": "Franklin"
                }
            ],
            ValueError,
            id="test user`s 'first_name' is numeric"
        )
    ]
)
def test_should_raise_exception(
    users: list[dict],
    expected_exception: type[Exception]
) -> None:
    with pytest.raises(expected_exception):
        restore_names(users)

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_input, expected_result",
    [
        (
            [{"first_name": None,
              "last_name": "Willis",
              "full_name": "Emily Willis"}],
            [{"first_name": "Emily",
              "last_name": "Willis",
              "full_name": "Emily Willis"}]
        ),
        (
            [{"last_name": "Dou",
              "full_name": "John Dou"}],
            [{"first_name": "John",
              "last_name": "Dou",
              "full_name": "John Dou"}],
        ),
    ],
    ids=[
        "First name set to None",
        "No first name",
    ]
)
def test_restore_names(user_input: list[dict],
                       expected_result: list[dict]
                       ) -> None:
    restore_names(user_input)
    assert user_input == expected_result

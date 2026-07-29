import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_user, expected_user",
    [
        (
            [{"first_name": None,
              "last_name": "Smith",
              "full_name": "John Smith"}],
            [{"first_name": "John",
              "last_name": "Smith",
              "full_name": "John Smith"}]
        ),
        (
            [{"first_name": None,
              "last_name": "Black",
              "full_name": "Alex Black"}],
            [{"first_name": "Alex",
              "last_name": "Black",
              "full_name": "Alex Black"}],
        ),
        (
            [{"first_name": "Gabriel",
              "last_name": "Suarez",
              "full_name": "Gabriel Suarez"}],
            [{"first_name": "Gabriel",
              "last_name": "Suarez",
              "full_name": "Gabriel Suarez"}],
        ),
        (
            [{"last_name": "Patterson",
              "full_name": "Kam Patterson"}],
            [{"first_name": "Kam",
              "last_name": "Patterson",
              "full_name": "Kam Patterson"}],
        )
    ]
)
def test_restore_names(input_user: list[dict],
                       expected_user: list[dict]
                       ) -> None:
    restore_names(input_user)
    assert input_user == expected_user

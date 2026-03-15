import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("user, expected",
                         [
                             (
                                 [{"full_name": "Artem Yur"}],
                                 [{"full_name": "Artem Yur", "first_name": "Artem"}],
                             ),
                             (
                                 [{"full_name": "Artem Yur", "first_name": None}],
                                 [{"full_name": "Artem Yur", "first_name": "Artem"}],
                             ),
                             (
                                 [{"full_name": "Artem Yur", "first_name": "Artem"}],
                                 [{"full_name": "Artem Yur", "first_name": "Artem"}],
                             ),
                         ],
                         )
def test_restore_names(user: list[dict], expected: list[dict]) -> None:
    restore_names(user)

    assert user == expected

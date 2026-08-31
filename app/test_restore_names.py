import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "before_dict, result_dict",
    [
        pytest.param(
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            id="First name is None",
        ),
        pytest.param(
            {
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            id="First name is missing",
        ),
    ],
)
def test_restore_names(before_dict: dict, result_dict: dict) -> None:
    users = [before_dict]

    restore_names(users)

    assert users == [result_dict]

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "name_before, fullname, expected_name",
    [
        pytest.param(
            None,
            "Jack Holy",
            "Jack",
            id="first name is None"
        ),

        pytest.param(
            None,
            "Bohdan Kryven",
            "Bohdan",
            id="first name is None"
        )
    ]
)
def test_restore_first_name(name_before, fullname, expected_name):
    users = [
        {
            "first_name": name_before,
            "full_name": fullname
        }
    ]

    restore_names(users)

    for user in users:
        assert user["first_name"] == expected_name


@pytest.mark.parametrize(
    "fullname, expected_name",
    [
        pytest.param(
            "Jack Holy",
            "Jack",
            id="first name is None"
        ),

        pytest.param(
            "Bohdan Kryven",
            "Bohdan",

        )
    ]
)
def test_add_first_name(fullname, expected_name):
    users = [
        {
            "full_name": fullname
        }
    ]

    restore_names(users)

    for user in users:
        assert user["first_name"] == expected_name

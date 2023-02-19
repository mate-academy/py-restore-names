import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    return [
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
        {
            "first_name": "Tomas",
            "last_name": "Anderson",
            "full_name": "Tomas Anderson",
        },
        {
            "first_name": "Andrea",
            "last_name": "Johnson",
            "full_name": "Andrea Johnson",
        }
    ]


@pytest.mark.parametrize(
    "test_user, output_first_name",
    [
        pytest.param({"first_name": "Jack",
                      "last_name": "Holy",
                      "full_name": "Jack Holy"},
                     "Jack", id="function doesnt change first name"),
        pytest.param({"last_name": "Adams",
                      "full_name": "Mike Adams"},
                     "Mike",
                     id="if there is no first name"),
        pytest.param({"first_name": None,
                      "last_name": "Anderson",
                      "full_name": "Tomas Anderson"},
                     "Tomas",
                     id="if first name is None"),
        pytest.param({"last_name": "Johnson",
                      "full_name": "  Andrea      Johnson      "},
                     "Andrea",
                     id="if full name has extra spaces")
    ]
)
def test_first_names(
        user_template: list,
        test_user: dict,
        output_first_name: str
) -> None:
    for i in range(4):
        user_template[i] = test_user
        restore_names(user_template)
        assert user_template[i]["first_name"] == output_first_name

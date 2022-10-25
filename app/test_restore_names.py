import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    user = [{"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            {"last_name": "Black",
             "full_name": "Dan Black"
             }]
    return user


def test_dictionary(user_template: list) -> None:
    with pytest.raises(TypeError):
        restore_names(user_template[0])


def test_the_user_is_dictionary(user_template: list) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"
    assert user_template[1]["first_name"] == "Dan"

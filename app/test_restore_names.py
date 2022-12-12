import pytest
from app.restore_names import restore_names

# write your tests here
# 1) if user is not a list
# 2) may be mock is function called once?


def test_correct_input_parameters() -> None:
    with pytest.raises(TypeError):
        restore_names({"name": "alice"})


@pytest.mark.parametrize(
    "users_list, result", [
        (
            [
                {"first_name": None,
                 "last_name": "Holy",
                 "full_name": "Jack Holy",
                 }
            ],
            [
                {"first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy",
                 }
            ],
        )
    ])
def test_none_first_name(users_list: list, result: any) -> None:
    restore_names(users_list)
    assert (users_list[0]["first_name"] == "Jack")


@pytest.mark.parametrize(
    "users_list, result", [
        (
            [
                {"last_name": "Liubchenko",
                 "full_name": "Oleksii Liubchenko",
                 }
            ],
            [
                {"first_name": "Oleksii",
                 "last_name": "Liubchenko",
                 "full_name": "Oleksii Liubchenko",
                 }
            ],
        )
    ])
def test_empty_first_name(users_list: list, result: any) -> None:
    restore_names(users_list)
    assert (users_list[0]["first_name"] == "Oleksii")

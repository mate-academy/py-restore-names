import pytest


from app.restore_names import restore_names


@pytest.fixture()
def sample_dict_in_the_list() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "firs_name": "FFF",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_checking_none_in_the_first_name(
        sample_dict_in_the_list: list[dict]) -> None:
    restore_names(sample_dict_in_the_list)
    assert all(user["first_name"] is not None
               for user in sample_dict_in_the_list)


def test_checking_first_name_in_users(
        sample_dict_in_the_list: list[dict]) -> None:
    restore_names(sample_dict_in_the_list)
    assert all("first_name" in user
               for user in sample_dict_in_the_list)

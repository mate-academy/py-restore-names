import pytest

from app.restore_names import restore_names


@pytest.fixture()
def user_dict_with_name() -> None:
    return [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    },
        {
        "first_name": "Chuck",
        "last_name": "Berry",
        "full_name": "Chuck Berry",
    }]


@pytest.fixture()
def user_dict_no_name() -> None:
    return [{
        "last_name": "Holy",
        "full_name": "Jack Holy",
    },
        {
        "first_name": None,
        "last_name": "Berry",
        "full_name": "Chuck Berry",
    }]


def test_first_name_restored(
    user_dict_with_name: list,
    user_dict_no_name: list
) -> None:
    restore_names(user_dict_no_name)
    assert user_dict_no_name[0] == user_dict_with_name[0]
    assert user_dict_no_name[1] == user_dict_with_name[1]

import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users():
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_after_fork_function(users):
    restore_names(users)
    assert users == [
        {'first_name': 'Jack', 'full_name': 'Jack Holy', 'last_name': 'Holy'},
        {'first_name': 'Mike', 'full_name': 'Mike Adams', 'last_name': 'Adams'}
    ]

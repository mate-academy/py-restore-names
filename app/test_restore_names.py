import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    ["users", "first_name"],
    [([{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }
    ], "Jack"), ([{
        "last_name": "Moraes",
        "full_name": "Luan Moraes",
    },
    ], "Luan"), ([{
        "first_name": None,
        "last_name": "Justino",
        "full_name": "Bento Justino",
    }
    ], "Bento"), ([{
        "first_name": "Bento",
        "last_name": "Justino",
        "full_name": "Bento Justino",
    }
    ], "Bento")]
)
def test_restore_first_name_logic(users: list[dict], first_name: str) -> None:
    restore_names(users)
    for user in users:
        assert user["first_name"] == first_name

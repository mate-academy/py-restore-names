import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_stupid() -> list:
    return [
        {
            "last_name": "Zhadan",
            "full_name": "Roman Zhadan"
        },
        {
            "first_name": None,
            "last_name": "Zhadan",
            "full_name": "Vika Zhadan"
        }
    ]


@pytest.fixture()
def user_normalize() -> list:
    return [
        {
            "first_name": "Roman",
            "last_name": "Zhadan",
            "full_name": "Roman Zhadan"
        },
        {
            "first_name": "Vika",
            "last_name": "Zhadan",
            "full_name": "Vika Zhadan"
        }
    ]


class TestRestoreNames:
    def test_correct_info(
            self,
            user_stupid: list[dict],
            user_normalize: list[dict]
    ) -> None:
        restore_names(user_stupid)

        assert user_stupid == user_normalize

import pytest

from app.restore_names import restore_names


class TestRestoreName:
    @pytest.mark.parametrize(
        "user, expected_dict",
        [
            pytest.param(
                [{"first_name": None, "full_name": "Jack Holy"}],
                [{"first_name": "Jack", "full_name": "Jack Holy"}],
                id="set correct `first_name` to users if it is None"
            ),
            pytest.param(
                [{"full_name": "Mike Adams"}],
                [{"first_name": "Mike", "full_name": "Mike Adams"}],
                id="set correct `first_name` to users who do not have it"
            )
        ]
    )
    def test_restore_name_work_correctly(self, user, expected_dict):
        restore_names(user)
        assert user == expected_dict

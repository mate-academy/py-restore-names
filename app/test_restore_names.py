import copy
import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "initial, expected",
        [
            pytest.param(
                [{"first_name": None, "last_name": "Holy",
                  "full_name": "Jack Holy"}],
                [{"first_name": "Jack", "last_name": "Holy",
                  "full_name": "Jack Holy"}],
                id="first_name is None"
            ),
            pytest.param(
                [{"last_name": "Adams", "full_name": "Mike Adams"}],
                [{"first_name": "Mike", "last_name": "Adams",
                  "full_name": "Mike Adams"}],
                id="missing first_name"
            ),
            pytest.param(
                [{"first_name": "Ann", "last_name": "Smith",
                  "full_name": "Ann Smith"}],
                [{"first_name": "Ann", "last_name": "Smith",
                  "full_name": "Ann Smith"}],
                id="first_name present"
            ),
            pytest.param(
                [{"first_name": None, "full_name": "Madonna"}],
                [{"first_name": "Madonna", "full_name": "Madonna"}],
                id="full_name is a single"
            ),
        ],
    )
    def test_restore_names_parametrized(
            self,
            initial: list[dict],
            expected: list[dict]
    ) -> None:
        users = copy.deepcopy(initial)
        restore_names(users)
        assert users == expected

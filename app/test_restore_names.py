import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "input_names, expected_result",
        [
            pytest.param(
                [{"first_name": None,
                  "last_name": "Holy",
                  "full_name": "Jack Holy"},
                 {"first_name": None,
                  "last_name": "Ass",
                  "full_name": "Pack Ass"}],
                [{"first_name": "Jack",
                  "last_name": "Holy",
                  "full_name": "Jack Holy"},
                 {"first_name": "Pack",
                  "last_name": "Ass",
                  "full_name": "Pack Ass"}],
                id="should restore first name if fist name is 'None'"),
            pytest.param(
                [{"last_name": "Adams",
                  "full_name": "Mike Adams"},
                 {"last_name": "Smith",
                  "full_name": "Vasya Smith"}],
                [{"first_name": "Mike",
                  "last_name": "Adams",
                  "full_name": "Mike Adams"},
                 {"first_name": "Vasya",
                  "last_name": "Smith",
                  "full_name": "Vasya Smith"}],
                id="should restore first name if no first name provided"),
            pytest.param(
                [{"first_name": None,
                  "last_name": "Holy",
                  "full_name": "Jack Holy"},
                 {"last_name": "Adams",
                  "full_name": "Mike Adams"}],
                [{"first_name": "Jack",
                  "last_name": "Holy",
                  "full_name": "Jack Holy"},
                 {"first_name": "Mike",
                  "last_name": "Adams",
                  "full_name": "Mike Adams"}],
                id="should restore first name if in list 2 different cases")
        ]
    )
    def test_restoring_names_correctly(
        self,
        input_names: list,
        expected_result: list
    ) -> None:
        restore_names(input_names)
        assert input_names == expected_result

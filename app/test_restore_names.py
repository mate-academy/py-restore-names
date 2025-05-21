import pytest
from app.restore_names import restore_names


class TestRestoreNames:

    @pytest.mark.parametrize("input_list, expected_list", [
        ([{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }, {"last_name": "Adams",
            "full_name": "Mike Adams"}, {
            "first_name": "Bill",
            "last_name": "Hanks",
            "full_name": "Bill Hanks"}
        ], [{"first_name": "Jack",
             "last_name": "Holy",
             "full_name": "Jack Holy"}, {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams", }, {
            "first_name": "Bill",
            "last_name": "Hanks",
            "full_name": "Bill Hanks"}])])
    def test_restore_names(
            self,
            input_list: list,
            expected_list: list
    ) -> None:
        restore_names(input_list)
        assert input_list == expected_list

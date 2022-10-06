import pytest
from app.restore_names import restore_names


class TestExpectListRestoreNames:

    def test_with_full_name(self):
        test_users = [
            {
                "first_name": None,
                "last_name": "Moris",
                "full_name": "Jim Moris",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
            {
                "first_name": "Terry",
                "last_name": None,
                "full_name": "Terry",
            },
            {
                "first_name": "Alis",
                "last_name": "Miller",
                "full_name": "Alis Miller"
            }
        ]

        expect_list = [
            {
                "first_name": "Jim",
                "last_name": "Moris",
                "full_name": "Jim Moris",
            },
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
            {
                "first_name": "Terry",
                "last_name": None,
                "full_name": "Terry",
            },
            {
                "first_name": "Alis",
                "last_name": "Miller",
                "full_name": "Alis Miller"
            }
        ]

        restore_names(test_users)

        assert test_users == expect_list


class TestErrorsRestoreNames:
    def test_without_full_name(self):
        team = [
            {
                "second_name": "Bill",
                "last_name": "Smoled",

            },
            {
                "second_name": None,
                "last_name": "Hemred",

            }
        ]

        with pytest.raises(KeyError):
            restore_names(team)

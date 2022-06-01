import pytest
from app.restore_names import restore_names

USERS_FOR_FIRST_TEST = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": None,
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]

USERS_FOR_SECOND_TEST = [
            {
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]

CORRECT_RESULT = [
                    {
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    },
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    },
                ]


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users, correct_list",
        [
            pytest.param(USERS_FOR_FIRST_TEST, CORRECT_RESULT)
        ]
    )
    def test_restore_names_when_first_name_is_None(self, users, correct_list):
        restore_names(users)
        assert users == correct_list, (
            f"Function 'restore_names' should change list : {users},"
            f"in correct list : {correct_list}"
        )

    @pytest.mark.parametrize(
        "users, correct_list",
        [
            pytest.param(USERS_FOR_SECOND_TEST, CORRECT_RESULT)
        ]
    )
    def test_restore_names_when_not_first_name(self, users, correct_list):
        restore_names(users)
        assert users == correct_list, (
            f"Function 'restore_names' should change list : {users},"
            f"in correct list : {correct_list}"
        )

    @pytest.mark.parametrize(
        "users",
        [
            pytest.param(USERS_FOR_FIRST_TEST)
        ]
    )
    def test_type_func_argument(self, users):
        assert isinstance(users, list), \
            f"{type(users)} - Not correct type argument, " \
            f"type argument must be 'list'"

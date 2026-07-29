import pytest

from typing import Any

from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users_list,"
        "recovery_users_list", [
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    }
                ],
                [
                    {
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    }
                ],
                id="test get list with 'first name' is None"
            ),
            pytest.param(
                [
                    {
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    },
                ],
                [
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    }
                ],
                id="test get list without 'first name'"
            )
        ]
    )
    def test_restore_names(
            self,
            users_list: list,
            recovery_users_list: list
    ) -> None:
        restore_names(users_list)

        assert users_list == recovery_users_list

    @pytest.mark.parametrize(
        "users_list", [
            pytest.param(
                [
                    {

                    }
                ],
                id="test get empty dict and should raising KeyError"
            )
        ]
    )
    def test_raising_key_errors_in_restore_names(
            self,
            users_list: list
    ) -> None:

        with pytest.raises(KeyError):
            restore_names(users_list)

    @pytest.mark.parametrize(
        "users_list", [
            pytest.param(
                [
                    "string"
                ],
                id="test get 'string' should raising TypeError"
            ),
            pytest.param(
                [
                    17
                ],
                id="test get 'integer' should raising TypeError"
            )

        ]
    )
    def test_raising_type_errors_in_restore_name(
            self,
            users_list: Any
    ) -> None:

        with pytest.raises(TypeError):
            restore_names(users_list)

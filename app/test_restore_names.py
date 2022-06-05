import pytest

from app.restore_names import restore_names


class TestAddFirstname:

    @pytest.mark.parametrize(
        "user,full_user",
        [
            (
                [
                    {
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    }
                ],
                [
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams"
                    }

                ]
            ),
            (
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
                ]
            )
        ]
    )
    def test_add_firstname(self, user, full_user):
        restore_names(user)
        assert user == full_user

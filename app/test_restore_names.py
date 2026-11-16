import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users, expected_result",
        [
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Lennon",
                        "full_name": "John Lennon",
                    },
                    {
                        "last_name": "Hendrix",
                        "full_name": "Jimi Hendrix",
                    },
                ],
                [
                    {
                        "first_name": "John",
                        "last_name": "Lennon",
                        "full_name": "John Lennon",
                    },
                    {
                        "first_name": "Jimi",
                        "last_name": "Hendrix",
                        "full_name": "Jimi Hendrix",
                    },
                ],
                id="restore missing and none first names"
            ),
            pytest.param(
                [
                    {
                        "first_name": "Harrier",
                        "last_name": "Du-Bois",
                        "full_name": "Harrier Du-Bois",
                    }
                ],
                [
                    {
                        "first_name": "Harrier",
                        "last_name": "Du-Bois",
                        "full_name": "Harrier Du-Bois",
                    }
                ],
                id="preserve existing first_name"
            ),
            pytest.param(
                [],
                [],
                id="test empty users list"
            ),
            pytest.param(
                [
                    {
                        "full_name": "Madonna",
                    }
                ],
                [
                    {
                        "first_name": "Madonna",
                        "full_name": "Madonna",
                    }
                ],
                id="test single word full name"
            ),
        ]
    )
    def test_restore_names(
        self,
        users: list[dict],
        expected_result: list[dict] 
    ) -> None:
        restore_names(users)
        assert users == expected_result

import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.fixture()
    def result_user(self):
        return [{
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith"
        }]

    @pytest.mark.parametrize(
        "test_user",
        [
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Smith",
                        "full_name": "John Smith"
                    }
                ],
                id="first name None"
            ),
            pytest.param(
                [
                    {
                        "last_name": "Smith",
                        "full_name": "John Smith"
                    }
                ],
                id="without first name"
            ),
        ]
    )
    def test_restore_names(self, test_user, result_user):
        restore_names(test_user)
        assert test_user == result_user

    def test_return_of_restore_name_function(self, result_user):
        assert restore_names(result_user) is None

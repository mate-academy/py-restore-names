import pytest

from app.restore_names import restore_names


class TestRestoreName:
    @pytest.fixture(scope="function")
    def user_template(self) -> list:
        return \
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ]

    @pytest.fixture(scope="function")
    def user_template_expected(self) -> list:
        return\
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ]

    def test_should_check_non_list_argument(self) -> None:
        with pytest.raises(TypeError):
            restore_names(None)

    def test_should_return_correct_name(self,
                                        user_template: list,
                                        user_template_expected: list) -> None:
        restore_names(user_template)
        assert user_template == user_template_expected

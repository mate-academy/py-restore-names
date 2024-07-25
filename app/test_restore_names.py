import pytest
from app.restore_names import restore_names


@pytest.fixture()
def temporary_list() -> list:
    yield [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_fix_dict_correctly(
        temporary_list: list
) -> None:
    restore_names(temporary_list)
    assert temporary_list == [
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
        "input_data, expected_error",
        [
            pytest.param(
                None,
                TypeError,
                id="should raise an error when None"
            ),
            pytest.param(
                {"a": "b"},
                TypeError,
                id="should raise an error when dict"
            ),
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                    },
                    {
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    },
                ],
                KeyError,
                id="should raise an error when not full_name"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            input_data: dict,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            restore_names(input_data)

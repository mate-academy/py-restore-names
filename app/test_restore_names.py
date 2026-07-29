import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "initial_list,expected_list",
    [
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
            id="when first_name in None"
        ),
        pytest.param(
            [
                {
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
            id="when dict doesn't have first_name"
        ),
        pytest.param(
            [
                {
                    "full_name": "Jack Holy",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "full_name": "Jack Holy",
                }
            ],
            id="when dict doesn't have last_name"
        ),
        pytest.param(
            [],
            [],
            id="when list is empty"
        )
    ]
)
def test_should_return_result_correctly(
        initial_list: list[dict],
        expected_list: list[dict]
) -> None:
    restore_names(initial_list)

    assert initial_list == expected_list


@pytest.mark.parametrize(
    "initial_element,expected_error",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                }
            ],
            KeyError,
            id="when dict doesn't have key `full_name`"
        ),
        pytest.param(
            [
                {
                }
            ],
            KeyError,
            id="empty dict is not valid value`"
        ),
        pytest.param(
            0,
            TypeError,
            id="number is not a valid type"
        )
    ]
)
def test_should_return_error_correctly(
        initial_element: list[dict],
        expected_error: any,
) -> None:
    with pytest.raises(expected_error):
        restore_names(initial_element)

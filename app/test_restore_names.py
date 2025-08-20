import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_sample, expected",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
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
                },
            ],
            id="should return base with filled first names if \
            'first_name' key value is None or no 'first_name' key",
        ),
        pytest.param(
            [
                {
                    "first_name": "Todd",
                    "last_name": "Howard",
                    "full_name": "Todd Howard",
                },
                {
                    "first_name": "Jeff",
                    "last_name": "Adriano",
                    "full_name": "Jeff Adriano",
                },
            ],
            [
                {
                    "first_name": "Todd",
                    "last_name": "Howard",
                    "full_name": "Todd Howard",
                },
                {
                    "first_name": "Jeff",
                    "last_name": "Adriano",
                    "full_name": "Jeff Adriano",
                },
            ],
            id="should do nothing if 'first_name' key is present and filled",
        ),
    ],
)
def test_with_different_params(
    users_sample: list[dict], expected: list[dict]
) -> None:
    restore_names(users_sample)
    assert users_sample == expected


@pytest.mark.parametrize(
    "users_sample, exception",
    [
        pytest.param(1, TypeError),
        pytest.param(None, TypeError),
        pytest.param(
            [
                {"first_name": None, "last_name": "Howard"},
            ],
            KeyError,
        ),
    ],
)
def test_raises_correct_exception(
    users_sample: list[dict], exception: type[Exception]
) -> None:
    with pytest.raises(exception):
        restore_names(users_sample)

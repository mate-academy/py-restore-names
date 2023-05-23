import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users",
    [
        ["Holy", "Jack"],
        "Holy, Jack",
        123456
    ]
)
def test_should_raise_error_if_input_has_wrong_type(
        users: list[str] | str | int
) -> None:
    with pytest.raises(TypeError):
        restore_names(users)


@pytest.fixture()
def users_template() -> list[dict]:
    return [
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


@pytest.fixture()
def result_template() -> list[dict]:
    return [
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


def test_should_make_new_first_name(
        users_template: list[dict],
        result_template: list[dict]
) -> None:
    restore_names(users_template)
    assert users_template == result_template

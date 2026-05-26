import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "names,expected",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            id="First name is None",
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
                },
            ],
            id="First name is absent",
        ),
    ]
)
def test_restore_names_if_name_is_none(
    names: list,
    expected: list
) -> None:
    restore_names(names)
    assert names[0]["first_name"] == expected[0]["first_name"]


@pytest.mark.parametrize(
    "names,expected",
    [
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
                },
            ],
            id="First name is absent",
        ),
    ]
)
def test_restore_names_if_name_is_absent(
    names: list,
    expected: list
) -> None:
    restore_names(names)
    assert names[0]["first_name"] == expected[0]["first_name"]

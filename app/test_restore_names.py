import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "before,name_field_values",
    [
        (
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
            ["Jack", "Mike"]
        )
    ]
)
def test_restore_names(
        before: list[dict],
        name_field_values: list[str]
) -> None:
    restore_names(before)
    after = before
    assert [person["first_name"] for person in after] == name_field_values

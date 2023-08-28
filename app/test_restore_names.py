import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "not_modified_list, modified_list",
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
            id="should have key 'first_name' and not None value"
        )
    ]
)
def test_restore_names(
        not_modified_list: list,
        modified_list: list,
) -> None:
    restore_names(not_modified_list)
    assert not_modified_list == modified_list

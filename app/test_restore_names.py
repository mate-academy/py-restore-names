import pytest


from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
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
            id=("'first_name' should be 'Jack' when 'first_name' is None"
                " and 'full_name' is 'Jack Holy'")
        ),
        pytest.param(
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            id=("'first_name' should be 'Mike' when 'full_name' is"
                " 'Mike Adams' and there is originally no 'first_name'")
        )
    ]
)
def test_restore_name(users: list, expected: list) -> None:
    restore_names(users)
    assert (users[0]["first_name"] == expected[0]["first_name"])

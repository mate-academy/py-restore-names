import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_list",
    [
        [
            {
                "last_name": "Griffin",
                "full_name": "Peter Griffin"
            },
            {
                "first_name": "Regina",
                "last_name": "Phalange",
                "full_name": "Regina Phalange"
            },
            {
                "first_name": None,
                "last_name": "Shartsev",
                "full_name": "Yehor Shartsev"
            },
            {
                "first_name": "Homer",
                "last_name": "Simpson",
                "full_name": "Homer Simpson"
            },
            {
                "last_name": "McConaughey",
                "full_name": "Matthew McConaughey"
            },
        ],
        [
            {
                "last_name": "Shartsev",
                "full_name": "Nazar Shartsev"
            },
            {
                "first_name": None,
                "last_name": "Shartsev",
                "full_name": "John Shartsev"
            },
            {
                "first_name": "Vasyl",
                "last_name": "Smutok",
                "full_name": "Vasyl Smutok"
            },
            {
                "first_name": None,
                "last_name": "Parker",
                "full_name": "Petro Parker"
            },
            {
                "last_name": "Obama",
                "full_name": "Barack Obama"
            },
        ]
    ]
)
def test_func_restores_names(users_list: list[dict]) -> None:
    result = restore_names(users_list)
    for user in users_list:
        assert user["first_name"] == user["full_name"].split()[0]
    assert result is None

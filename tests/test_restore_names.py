import pytest

from app.restore_names import restore_names


def test_should_return_none():
    assert restore_names([]) is None


@pytest.mark.parametrize(
    "users, expected",
    [
        ([
             {
                 "first_name": None,
                 "last_name": "Holy",
                 "full_name": "Jack Holy",
             },
             {
                 "first_name": None,
                 "last_name": "Zhidkov",
                 "full_name": "Alex Zhidkov",
             }
         ],
         [
             {
                 "first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy",
             },
             {
                 "first_name": "Alex",
                 "last_name": "Zhidkov",
                 "full_name": "Alex Zhidkov",
             }
         ]),
    ],
)
def test_when_first_name_is_none(users, expected):
    restore_names(users)
    for test in range(len(users)):
        assert users[test]["first_name"] == expected[test]["first_name"]


@pytest.mark.parametrize(
    "users, expected",
    [
        ([
             {
                 "last_name": "Holy",
                 "full_name": "Jack Holy",
             },
             {
                 "last_name": "Zhidkov",
                 "full_name": "Alex Zhidkov",
             }
         ],
         [
             {
                 "first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy",
             },
             {
                 "first_name": "Alex",
                 "last_name": "Zhidkov",
                 "full_name": "Alex Zhidkov",
             }
         ]),
    ],
)
def test_when_first_name_is_not_exist(users, expected):
    restore_names(users)
    for test in range(len(users)):
        assert users[test]["first_name"] == expected[test]["first_name"]


@pytest.mark.parametrize(
    "users, expected",
    [
        ([
             {
                 "first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy",
             },
             {
                 "first_name": "Alex",
                 "last_name": "Zhidkov",
                 "full_name": "Alex Zhidkov",
             }
         ],
         [
             {
                 "first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy",
             },
             {
                 "first_name": "Alex",
                 "last_name": "Zhidkov",
                 "full_name": "Alex Zhidkov",
             }
         ]),
    ],
)
def test_when_all_right(users, expected):
    restore_names(users)
    for test in range(len(users)):
        assert users[test]["first_name"] == expected[test]["first_name"]

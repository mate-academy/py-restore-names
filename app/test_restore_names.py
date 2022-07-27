import pytest
from app.restore_names import restore_names


def test_correct_first_name_when_first_name_is_equal_to_None():
    assert restore_names([
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]) == [
               {
                   "first_name": "Jack",
                   "last_name": "Holy",
                   "full_name": "Jack Holy",
               }
           ]


def test_correct_first_name_when_first_name_is_not_in_dict():
    assert restore_names([
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]) == [
               {
                   "first_name": "Mike",
                   "last_name": "Adams",
                   "full_name": "Mike Adams",
               },
           ]

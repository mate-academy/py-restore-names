import pytest
from app.restore_names import restore_names


@pytest.fixture()
def person_names() -> None:
    return restore_names([{"first_name": None,
                           "last_name": "Holy",
                           "full_name": "Jack Holy"},
                          {"last_name": "Adams",
                           "full_name": "Mike Adams"},
                          {"first_name": None,
                           "last_name": "Smith",
                           "full_name": "Andrew Smith"}])


def test_should_make_correct_first_name(person_names: callable) -> None:
    list_of_dicts = [{"first_name": None,
                      "last_name": "Holy",
                      "full_name": "Jack Holy"},
                     {"last_name": "Adams",
                      "full_name": "Mike Adams"},
                     {"first_name": None,
                      "last_name": "Smith",
                      "full_name": "Andrew Smith"}]
    list_of_expected = [{"first_name": "Jack",
                         "last_name": "Holy",
                         "full_name": "Jack Holy"},
                        {"first_name": "Mike",
                         "last_name": "Adams",
                         "full_name": "Mike Adams"},
                        {"first_name": "Andrew",
                         "last_name": "Smith",
                         "full_name": "Andrew Smith"}]
    restore_names(list_of_dicts)
    assert list_of_dicts == list_of_expected

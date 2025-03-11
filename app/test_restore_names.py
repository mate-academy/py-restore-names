import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("initial_dict, expected_dict",
                         [
                             pytest.param(
                                 [
                                     {
                                         "first_name": None,
                                         "last_name": "Holy",
                                         "full_name": "Jack Holy"
                                     }
                                 ],
                                 [
                                     {"first_name": "Jack",
                                      "last_name": "Holy",
                                      "full_name": "Jack Holy"
                                      }
                                 ],
                                 id="should_fill_first_name"
                             ),
                             pytest.param(
                                 [
                                     {
                                         "last_name": "Holy",
                                         "full_name": "Jack Holy"
                                     }
                                 ],
                                 [
                                     {"first_name": "Jack",
                                      "last_name": "Holy",
                                      "full_name": "Jack Holy"
                                      }
                                 ],
                                 id="should_create_and_fill_first_name"
                             ),
                         ]
                         )
def test_restore_names_without_first_name(initial_dict: dict,
                                          expected_dict: dict) -> None:
    restore_names(initial_dict)
    assert initial_dict == expected_dict

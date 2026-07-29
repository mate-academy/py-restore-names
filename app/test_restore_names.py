import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "damaged_list, restored_list",
    [pytest.param([{"first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"}],
                  [{"first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"}],
                  id="firstname added if it None"
                  ),
     pytest.param([{"last_name": "Adams",
                    "full_name": "Mike Adams"}],
                  [{"first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"}],
                  id="firstname added if it doesn't exist")])
def test_restored_data(damaged_list, restored_list):
    restore_names(damaged_list)
    assert damaged_list == restored_list

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("initial_value, expected_value", [
                         pytest.param([{
                             "last_name": "Holy",
                             "full_name": "Jack Holy",
                         }],
                             [{
                                 "first_name": "Jack",
                                 "last_name": "Holy",
                                 "full_name": "Jack Holy",
                             }],
                             id="Restore only missing names"
                         ),
                         pytest.param([{
                             "first_name": None,
                             "last_name": "Holy",
                             "full_name": "Jack Holy",
                         }],
                             [{
                                 "first_name": "Jack",
                                 "last_name": "Holy",
                                 "full_name": "Jack Holy",
                             }],
                             id="Restore only missing names")]
                         )
def test_restore_names(initial_value: list[dict],
                       expected_value: list[dict]) -> None:
    restore_names(initial_value)
    assert initial_value == expected_value

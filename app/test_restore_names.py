import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "current_base, correct_base_expected",
    [
        ([{
          "first_name": None,
          "last_name": "Holy",
          "full_name": "Jack Holy",
          }],
         [{
          "first_name": "Jack",
          "last_name": "Holy",
          "full_name": "Jack Holy",
          }]
         ),
        ([{
          "last_name": "Adams",
          "full_name": "Mike Adams",
          }],
         [{
          "first_name": "Mike",
          "last_name": "Adams",
          "full_name": "Mike Adams",
          }]
         )

    ]
)
def test_restore_names(current_base: list[dict],
                       correct_base_expected: list[dict]
                       ) -> None:
    restore_names(current_base)
    assert current_base == correct_base_expected

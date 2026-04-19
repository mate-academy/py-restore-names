import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("inserted_list, expected", [
    ([{"first_name": None,
       "last_name": "Snow",
       "full_name": "John Snow"},
      {"last_name": "Lanister",
       "full_name": "Jame Lanister"}],
     [{"first_name": "John",
       "last_name": "Snow",
       "full_name": "John Snow"},
      {"first_name": "Jame",
       "last_name": "Lanister",
       "full_name": "Jame Lanister"}]),
])
def test_restore_names(inserted_list: list[dict],
                       expected: list[dict]) -> None:
    restore_names(inserted_list)
    assert inserted_list == expected

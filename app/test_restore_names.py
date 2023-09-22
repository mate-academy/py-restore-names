import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("users, expected", [
    ([{
        "first_name": "John",
        "last_name": "Konor",
        "full_name": "John Konor"
    }],
     [{
         "first_name": "John",
         "last_name": "Konor",
         "full_name": "John Konor"
     }]),
    ([{
        "first_name": None,
        "last_name": "Konor",
        "full_name": "John Konor"
    }],
     [{
         "first_name": "John",
         "last_name": "Konor",
         "full_name": "John Konor"
     }]),
    ([{
        "last_name": "Konor",
        "full_name": "John Konor"
    }],
     [{
         "first_name": "John",
         "last_name": "Konor",
         "full_name": "John Konor"
     }])
])
def test_restore_name(users, expected):
    restore_names(users)
    assert users == expected

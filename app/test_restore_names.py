import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "ls,first_name,num_of_ls",
    [
        (
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            "Jack",
            0
        ),

        (
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Adam Holy",
            }],
            "Adam",
            1
        ),
    ]
)
def test_s(ls, first_name, num_of_ls):
    restore_names(ls)
    assert first_name in ls[num_of_ls].get("first_name")

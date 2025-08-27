import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(

    "name_list, result",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "John Smith"
                },
                {
                    "last_name": "Smith",
                    "full_name": "John Smith"
                },

            ],
            {"first_name": "John"}
        ),

        (
            [

                {
                    "last_name": "Black",
                    "full_name": "Bob Black"
                },
                {
                    "first_name": None,
                    "last_name": "Black",
                    "full_name": "Bob Black"
                },
            ],
            {"first_name": "Bob"}
        )
    ]
)
def test_restore_names(name_list: list, result: dict) -> None:
    restore_names(name_list)

    for name_dict in name_list:
        assert name_dict["first_name"] == result["first_name"]

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "data_dict,r_dict",
    [
        ([{"first_name": None, "last_name": "Ho", "full_name": "Jack Ho"},
          {"first_name": "Mike", "last_name": "Ad", "full_name": "Mike Ad"}
          ], [
            {"first_name": "Jack", "last_name": "Ho", "full_name": "Jack Ho"},
            {"first_name": "Mike", "last_name": "Ad", "full_name": "Mike Ad"}
        ]),
        ([{"last_name": "Ho", "full_name": "Jack Ho"},
          {"first_name": None, "last_name": "Ad", "full_name": "Mike Ad"}
          ], [
            {"first_name": "Jack", "last_name": "Ho", "full_name": "Jack Ho"},
            {"first_name": "Mike", "last_name": "Ad", "full_name": "Mike Ad"}
        ]),
        ([], [])
    ],
    ids=[
        "test_None_name",
        "test_no_first_name",
        "test_no_dicts"
    ]
)
def test_restore_names(data_dict: list[dict],
                       r_dict: list[dict]
                       ) -> None:
    restore_names(data_dict)
    assert data_dict == r_dict, (f"should return "
                                 f"{r_dict}, but returns"
                                 f" {restore_names(data_dict)}")

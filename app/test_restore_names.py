import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("list_users, result",
                         [([{"first_name": "Illia",
                            "full_name": "Illia Petukhov"}], "Illia"),
                          ([{"first_name": None,
                            "full_name": "Illia Petukhov"}], "Illia"),
                          ([{"first_nameq": "",
                            "full_name": "Illia Petukhov"}], "Illia")])
def test_universal(list_users: list[dict], result: str) -> None:
    restore_names(list_users)
    for user in list_users:
        assert user["first_name"] == result

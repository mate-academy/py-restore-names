import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_list,result_name",
    [
        pytest.param([{
            "last_name": "Adams", "full_name": "John Adams"}],
            "John", id="first_name_does_not_exist"),
        pytest.param([{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"}],
            "Jack", id="first_name_is_None")
    ])
def test_restore_names(user_list: list[dict], result_name: str) -> None:
    restore_names(user_list)
    assert user_list[0]["first_name"] == result_name

import pytest


@pytest.fixture()
def users() -> bool:
    return users == [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]



def test_restore_names(users) -> None:
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            assert user["first_name"] == user["full_name"].split()[0]
    #
    #
    #
    # @pytest.mark.parametrize(
    #     "cat_age, dog_age",
    #     [
    #         ("k", 12),
    #         (12, "k"),
    #         ("k", "k"),
    #         ({"k"}, {"k"}),
    #         (["k"], ["k"])
    #     ]
    # )
    # def test_correct_types_value_get_human_age(
    #         self,
    #         cat_age: int,
    #         dog_age: int
    # ) -> None:
    #
    #     with pytest.raises(TypeError):
    #         get_human_age(cat_age, dog_age)

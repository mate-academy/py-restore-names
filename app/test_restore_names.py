from pytest import fixture


from app.restore_names import restore_names


@fixture()
def user_template() -> list[dict]:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_restore_name_when_first_name_doesnt_exist(
        user_template: list[dict]
) -> None:
    user_template[0].pop("first_name")
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_restore_name_when_first_name_is_none(
        user_template: list[dict]
) -> None:
    user_template[0]["first_name"] = None
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"


def test_do_nothing_when_first_name_is_correct(
        user_template: list[dict]
) -> None:
    restore_names(user_template)
    assert user_template[0]["first_name"] == "Jack"

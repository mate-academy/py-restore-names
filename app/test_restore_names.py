import pytest
from app.restore_names import restore_names


def test_given_not_a_list() -> None:
    with pytest.raises(TypeError):
        restore_names("not a list")


def test_list_contains_dictionaries() -> None:
    test_input = [{"full_name": "John Doe"}, {"full_name": "Jane Doe"}]
    try:
        restore_names(test_input)
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")


def test_dictionaries_have_full_name_key() -> None:
    test_input = [{"full_name": "John Doe"}, {"full_name": "Jane Doe"}]
    restore_names(test_input)
    for user in test_input:
        assert "full_name" in user,\
            "Dictionary does not contain 'full_name' key"


def test_full_name_is_string() -> None:
    test_input = [{"full_name": "John Doe"}, {"full_name": "Jane Doe"}]
    restore_names(test_input)
    for user in test_input:
        assert isinstance(
            user["full_name"], str
        ), "'full_name' is not a string"


def test_full_name_contains_two_words() -> None:
    test_input = [{"full_name": "John Doe"}, {"full_name": "Jane Doe"}]
    restore_names(test_input)
    for user in test_input:
        assert len(
            user["full_name"].split()
        ) == 2, "'full_name' does not contain two words"


def test_function_returns_none() -> None:
    test_input = [{"full_name": "John Doe"}, {"full_name": "Jane Doe"}]
    result = restore_names(test_input)
    assert result is None, "Function does not return None"


@pytest.mark.parametrize("input_dict, expected", [
    ({"full_name": "John Doe", "first_name": "John"}, "John"),
    ({"full_name": "John Doe"}, "John"),
    ({"full_name": "John Doe", "first_name": None}, "John"),
    ({"full_name": "John Doe", "first_name": ""}, "John")
])
def test_first_name_is_str_if_present(
        input_dict: dict,
        expected: str
) -> None:
    restore_names([input_dict])
    assert isinstance(
        input_dict["first_name"], str
    ), "'first_name' is not a string"
    assert input_dict["first_name"] == expected,\
        (f"Expected 'first_name' to be {expected}, "
         f"got {input_dict['first_name']}")

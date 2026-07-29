import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "actual_result,expected_result",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Doe",
                    "full_name": "John Doe",
                },
                {
                    "first_name": "Bob",
                    "last_name": "Smith",
                    "full_name": "Bob Smith",
                },
                {
                    "first_name": "Petro",
                    "last_name": "Schur",
                    "full_name": "Petro Schur",
                }],
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                },
                {
                    "first_name": "Bob",
                    "last_name": "Smith",
                    "full_name": "Bob Smith",
                },
                {
                    "first_name": "Petro",
                    "last_name": "Schur",
                    "full_name": "Petro Schur",
                }
            ], id="should return user with first"
                  " name when first name is None"),
        pytest.param([
            {
                "last_name": "Doe",
                "full_name": "John Doe",
            },
            {
                "first_name": "Bob",
                "last_name": "Smith",
                "full_name": "Bob Smith",
            },
            {
                "first_name": "Petro",
                "last_name": "Schur",
                "full_name": "Petro Schur"}],
            [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            },
            {
                "first_name": "Bob",
                "last_name": "Smith",
                "full_name": "Bob Smith",
            },
            {
                "first_name": "Petro",
                "last_name": "Schur",
                "full_name": "Petro Schur",
            }
        ], id="should return user with first name "
              "when there is no first name key"
        ),
        pytest.param([
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            },
            {
                "first_name": "Bob",
                "last_name": "Smith",
                "full_name": "Bob Smith",
            },
            {
                "first_name": "Petro",
                "last_name": "Schur",
                "full_name": "Petro Schur"}],
            [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            },
            {
                "first_name": "Bob",
                "last_name": "Smith",
                "full_name": "Bob Smith",
            },
            {
                "first_name": "Petro",
                "last_name": "Schur",
                "full_name": "Petro Schur",
            }
        ], id="should return user with first name when "
              "there already is first name in user"
        ),

    ]
)
def test_restore_names(
        actual_result: list[dict],
        expected_result: list[dict]
) -> None:
    restore_names(actual_result)
    assert actual_result == expected_result

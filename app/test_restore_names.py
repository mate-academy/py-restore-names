import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("users_input,users_output",
                         [
                             pytest.param(
                                 [
                                     {
                                         "last_name": "Adams",
                                         "full_name": "Mike Adams"
                                     }
                                 ],
                                 [
                                     {
                                         "first_name": "Mike",
                                         "last_name": "Adams",
                                         "full_name": "Mike Adams",
                                     }
                                 ],
                                 id="function adds first name if it`s lost"
                             ),
                             pytest.param(
                                 [
                                     {
                                         "first_name": None,
                                         "last_name": "Adams",
                                         "full_name": "Mike Adams"
                                     }
                                 ],
                                 [
                                     {
                                         "first_name": "Mike",
                                         "last_name": "Adams",
                                         "full_name": "Mike Adams"
                                     }
                                 ],
                                 id="function adds first name if it`s None"
                             ),
                             pytest.param(
                                 [
                                     {
                                         "first_name": "Mike",
                                         "last_name": "Adams",
                                         "full_name": "Mike Adams"
                                     },
                                     {
                                         "last_name": "Holy",
                                         "full_name": "Jack Holy",
                                     },
                                 ],
                                 [
                                     {
                                         "first_name": "Mike",
                                         "last_name": "Adams",
                                         "full_name": "Mike Adams"
                                     },
                                     {
                                         "first_name": "Jack",
                                         "last_name": "Holy",
                                         "full_name": "Jack Holy",
                                     }
                                 ],
                                 id="function can proses several users"
                             ),
                             pytest.param(
                                 [
                                     {
                                         "first_name": "Mike",
                                         "last_name": "Adams",
                                         "full_name": "Mike Adams"
                                     },
                                 ],
                                 [
                                     {
                                         "first_name": "Mike",
                                         "last_name": "Adams",
                                         "full_name": "Mike Adams",
                                     },
                                 ],
                                 id="function doesn't change first name"
                             ),
                             pytest.param(
                                 [],
                                 [],
                                 id="function returns [] when input is []"
                             )

                         ]
                         )
def test_return_expected_values(
        users_input: list[dict],
        users_output: list[dict]
) -> None:
    restore_names(users_input)
    print("something")
    assert users_input == users_output

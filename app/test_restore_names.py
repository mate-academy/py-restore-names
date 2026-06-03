import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "name, result",
    [
        ([{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"}],
         [{
             "first_name": "Jack",
             "last_name": "Holy",
             "full_name": "Jack Holy"}]),
        ([{
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams"}],
         [{
             "first_name": "Mike",
             "last_name": "Adams",
             "full_name": "Mike Adams"}]),
    ]
)
def test_restore_only_none_names(name: List[dict], result: List[dict]) -> None:
    restore_names(name)
    assert name == result


@pytest.mark.parametrize(
    "name, result",
    [
        ([{
            "last_name": "Stark",
            "full_name": "Tony Stark"}],
         [{
             "first_name": "Tony",
             "last_name": "Stark",
             "full_name": "Tony Stark"}]),
        ([{
            "last_name": "Wilson",
            "full_name": "Wade Wilson"}],
         [{
             "first_name": "Wade",
             "last_name": "Wilson",
             "full_name": "Wade Wilson"}]),
    ]
)
def test_restore_only_missing_names(
        name: List[dict],
        result: List[dict]
) -> None:
    restore_names(name)
    assert name == result

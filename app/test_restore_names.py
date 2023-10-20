# import pytest
# from app.restore_names import restore_names
#
#
# @pytest.mark.parametrize(
#     "user, expected_user",
#     [
#         (
#             [
#                 {
#                     "first_name": None,
#                     "last_name": "Holy",
#                     "full_name": "Jack Holy",
#                 },
#                 {
#                     "last_name": "Adams",
#                     "full_name": "Mike Adams",
#                 },
#             ],
#             [
#                 {
#                     "first_name": "Jack",
#                     "last_name": "Holy",
#                     "full_name": "Jack Holy",
#                 },
#                 {
#                     "first_name": "Mike",
#                     "last_name": "Adams",
#                     "full_name": "Mike Adams"
#                 }
#
#             ]
#         )
#     ]
#
#
# )
# def test_restore_names(user: list[dict], expected_user: list[dict]):
#     restore_names(user)
#     assert user == expected_user
#
#
# @pytest.mark.parametrize(
#     "user",
#     [
#         [{1: 5}],
#         [{2: "some"}],
#         [{"some": 34}]
#     ]
# )
# def test_type_restore_names(user: list[dict]):
#     with pytest.raises(KeyError):
#         restore_names(user)

from unittest import TestCase
from app.restore_names import restore_names


class TestDictUsers(TestCase):

    def setUp(self) -> None:
        self.user = ([
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ])
        restore_names(self.user)
        print(self.user)

    def test_chek_first_name(self) -> None:
        user = self.user[0]
        self.assertEqual(user["first_name"], "Jack")

    def test_move_chek_first_name(self) -> None:
        user = self.user[0]
        user["first_name"] = "Denys"
        self.assertEqual(user["first_name"], "Denys")

    def test_check_keys(self) -> None:
        user = self.user[0]
        self.assertEqual(user["first_name"], "Jack")
        self.assertEqual(user["last_name"], "Holy")
        self.assertEqual(user["full_name"], "Jack Holy")

    def test_type_restore_names(self) -> None:
        with self.assertRaises(TypeError):
            restore_names([{2: "some"}])

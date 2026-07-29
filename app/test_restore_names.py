from app.restore_names import restore_names
from typing import Dict, List
import unittest


class TestRestoreNames(unittest.TestCase):

    def test_users_with_none_first_name(self) -> None:
        users: List[Dict[str, str]] = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": None,
                "last_name": "Doe",
                "full_name": "Jane Doe",
            },
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Jack")
        self.assertEqual(users[1]["first_name"], "Jane")

    def test_users_without_first_name_field(self) -> None:
        users: List[Dict[str, str]] = [
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
            {
                "last_name": "Smith",
                "full_name": "John Smith",
            },
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Mike")
        self.assertEqual(users[1]["first_name"], "John")

    def test_users_with_existing_first_name(self) -> None:
        users: List[Dict[str, str]] = [
            {
                "first_name": "Existing",
                "last_name": "Name",
                "full_name": "Existing Name",
            },
            {
                "first_name": "Already",
                "last_name": "Set",
                "full_name": "Already Set",
            },
        ]

        original_users: List[Dict[str, str]] = users.copy()

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Existing")
        self.assertEqual(users[1]["first_name"], "Already")
        self.assertEqual(users, original_users)

    def test_mixed_users(self) -> None:
        users: List[Dict[str, str]] = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
            {
                "first_name": "Keep",
                "last_name": "This",
                "full_name": "Keep This",
            },
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Jack")
        self.assertEqual(users[1]["first_name"], "Mike")
        self.assertEqual(users[2]["first_name"], "Keep")

    def test_empty_list(self) -> None:
        users: List[Dict[str, str]] = []

        restore_names(users)

        self.assertEqual(users, [])

    def test_multiple_word_first_name(self) -> None:
        users: List[Dict[str, str]] = [
            {
                "first_name": None,
                "full_name": "Mary Jane Watson",
            },
            {
                "first_name": None,
                "full_name": "Jean-Luc Picard",
            },
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Mary")
        self.assertEqual(users[1]["first_name"], "Jean-Luc")

    def test_single_word_full_name(self) -> None:
        users: List[Dict[str, str]] = [
            {
                "first_name": None,
                "full_name": "Madonna",
            },
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Madonna")

    def test_other_fields_preserved(self) -> None:
        users: List[Dict[str, str]] = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
                "age": "30",
                "email": "jack@example.com",
            },
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Jack")
        self.assertEqual(users[0]["last_name"], "Holy")
        self.assertEqual(users[0]["age"], "30")
        self.assertEqual(users[0]["email"], "jack@example.com")
        self.assertEqual(users[0]["full_name"], "Jack Holy")

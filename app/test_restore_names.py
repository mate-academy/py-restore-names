import pytest
from app.restore_names import restore_names

import unittest


class TestRestore(unittest.TestCase):
    def test_if_first_name_none(self):
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]
        expected = [
              {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
              },
              {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
              },
            ]
        restore_names(users)
        self.assertEqual(users, expected)

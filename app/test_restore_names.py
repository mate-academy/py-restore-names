import pytest

from unittest import TestCase
from app.restore_names import restore_names


class TestNames(TestCase):
    def setUp(self) -> None:
        self.users = [
          {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
          }
        ]

    def test_when_first_name_is_None(self):
        restore_names(self.users)
        assert self.users[0]["first_name"] == "Jack"

    def test_when_first_name_is_deleted(self):
        del self.users[0]["first_name"]
        restore_names(self.users)
        assert self.users[0]["first_name"] == "Jack"

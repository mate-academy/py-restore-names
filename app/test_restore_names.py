import unittest
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):
    def test_restore_names(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": None,
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]

        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Jack")
        self.assertEqual(users[1]["first_name"], "Mike")


if __name__ == "__main__":
    unittest.main()

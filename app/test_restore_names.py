from app.restore_names import restore_names


class TestRestoreNames:
    def test_restore_first_name_when_none(self) -> None:
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

        restore_names(users)

        assert users[0]["first_name"] == "Jack"
        assert users[0]["last_name"] == "Holy"
        assert users[0]["full_name"] == "Jack Holy"
        assert users[1]["first_name"] == "Mike"
        assert users[1]["last_name"] == "Adams"
        assert users[1]["full_name"] == "Mike Adams"

    def test_restore_first_name_when_missing(self) -> None:
        users = [
            {
                "last_name": "Smith",
                "full_name": "John Smith",
            },
            {
                "first_name": "Jane",
                "last_name": "Doe",
                "full_name": "Jane Doe",
            },
        ]

        restore_names(users)

        assert users[0]["first_name"] == "John"
        assert users[0]["last_name"] == "Smith"
        assert users[0]["full_name"] == "John Smith"
        assert users[1]["first_name"] == "Jane"
        assert users[1]["last_name"] == "Doe"
        assert users[1]["full_name"] == "Jane Doe"

    def test_do_not_change_existing_first_name(self) -> None:
        users = [
            {
                "first_name": "Alice",
                "last_name": "Johnson",
                "full_name": "Alice Johnson",
            },
            {
                "first_name": "Bob",
                "last_name": "Brown",
                "full_name": "Bob Brown",
            },
        ]

        original_users = [
            {
                "first_name": "Alice",
                "last_name": "Johnson",
                "full_name": "Alice Johnson",
            },
            {
                "first_name": "Bob",
                "last_name": "Brown",
                "full_name": "Bob Brown",
            },
        ]

        restore_names(users)

        assert users == original_users

    def test_mixed_cases(self) -> None:
        users = [
            {
                "first_name": "Alice",
                "last_name": "Johnson",
                "full_name": "Alice Johnson",
            },
            {
                "first_name": None,
                "last_name": "Smith",
                "full_name": "Bob Smith",
            },
            {
                "last_name": "Brown",
                "full_name": "Charlie Brown",
            },
            {
                "first_name": "David",
                "last_name": "Wilson",
                "full_name": "David Wilson",
            },
        ]

        restore_names(users)

        assert users[0]["first_name"] == "Alice"
        assert users[1]["first_name"] == "Bob"
        assert users[2]["first_name"] == "Charlie"
        assert users[3]["first_name"] == "David"

    def test_empty_list(self) -> None:
        users = []
        restore_names(users)

        assert users == []

    def test_single_name_in_full_name(self) -> None:
        users = [
            {
                "last_name": "Madonna",
                "full_name": "Madonna",
            },
        ]

        restore_names(users)

        assert users[0]["first_name"] == "Madonna"

    def test_multiple_words_in_full_name(self) -> None:
        users = [
            {
                "last_name": "van der Berg",
                "full_name": "Jan van der Berg",
            },
        ]

        restore_names(users)

        assert users[0]["first_name"] == "Jan"

    def test_function_returns_none(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Test",
                "full_name": "Test User",
            },
        ]

        result = restore_names(users)

        assert result is None
        assert users[0]["first_name"] == "Test"

    def test_preserve_other_fields(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Doe",
                "full_name": "John Doe",
                "email": "john@example.com",
                "age": 30,
            },
        ]

        restore_names(users)

        assert users[0]["first_name"] == "John"
        assert users[0]["last_name"] == "Doe"
        assert users[0]["full_name"] == "John Doe"
        assert users[0]["email"] == "john@example.com"
        assert users[0]["age"] == 30

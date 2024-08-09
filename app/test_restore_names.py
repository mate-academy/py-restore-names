from app.restore_names import restore_names

def test_restore_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Shevchenko",
            "full_name": "Sasha Shevchenko"},
        {
            "last_name": "Koval",
            "full_name": "Ivan Koval"},
        {
            "first_name": "Mykola",
            "last_name": "Syvchenko",
            "full_name": "Mykola Syvchenko"},
    ]
    restore_names(users)
    assert users == [
        {
            "first_name": "Sasha",
            "last_name": "Shevchenko",
            "full_name": "Sasha Shevchenko"},
        {
            "first_name": "Ivan",
            "last_name": "Koval",
            "full_name": "Ivan Koval"},
        {
            "first_name": "Mykola",
            "last_name": "Syvchenko",
            "full_name": "Mykola Syvchenko"},
    ]

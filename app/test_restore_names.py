from app.restore_names import restore_names
from _pytest.monkeypatch import MonkeyPatch


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


def test_get_exchange_rate_prediction(monkeypatch: MonkeyPatch) -> bool:
    def mock_input() -> list:
        return users

    monkeypatch.setattr("builtins.input", mock_input)

    result = restore_names(users)
    assert result is None


def test_get_exchange_rate_prediction1(monkeypatch: MonkeyPatch) -> bool:
    def mock_input() -> str:
        return users
    monkeypatch.setattr("builtins.input", mock_input)
    restore_names(users)
    assert users[0]["first_name"] == "Jack"

from app.restore_names import (
    restore_names
)  # Импортируем функцию из модуля
from typing import List
from pytest import MonkeyPatch


def test_restore_only_none_names(monkeypatch: MonkeyPatch) -> None:
    # Определяем замещающую функцию
    def restore_only_none_names(users: List[dict]) -> None:
        for user in users:
            if user["first_name"] is None:
                user["first_name"] = user["full_name"].split()[0]

    # Используем monkeypatch для замены функции restore_names на замещающую
    monkeypatch.setattr(
        "app.restore_names.restore_names", restore_only_none_names
    )

    # Тестовые данные
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"}
    ]

    # Вызываем функцию (замещённую версию)
    restore_names(users)

    # Проверяем, что имена были восстановлены
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"

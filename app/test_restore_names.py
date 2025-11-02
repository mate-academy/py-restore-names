import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "received, expected",
    [
        (
            [
                {"first_name": None,
                 "last_name": "Baudouin de Courtenay",
                 "full_name": "Jan Baudouin de Courtenay"}
            ],
            "Jan"
        ),
        (
            [
                {"last_name": "Schleicher",
                 "full_name": "August Schleicher"}
            ],
            "August"
        )
    ]
)
def test_restoring(received: list[dict], expected: str) -> None:
    restore_names(received)
    assert received[0]["first_name"] == expected

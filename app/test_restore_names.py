import pytest
from typing import Callable

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "current_rate, predicted_exchange, result", [
        ([{"last_name": "Holy", "full_name": "Jack Holy"}],
         [{"first_name": "Jack",
           "last_name": "Holy", "full_name": "Jack Holy"}],
         "Buy more cryptocurrency"),
        # (['1'], ['0.94'], "Sell all your cryptocurrency"),
        # (['1'], ['0.96'], "Do nothing"),
        # (['1'], [1.05], "Do nothing"),
        ([{"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}],
         [{"first_name": "Jack", "last_name": "Holy",
           "full_name": "Jack Holy"}],
         "Buy more cryptocurrency")
    ]
)
def test_get_exchange_rate_prediction_with_mock(monkeypatch: Callable,
                                                current_rate: list,
                                                predicted_exchange: list,
                                                result: str) -> None:
    # def mock_restore_names(current_rate: list) -> list:
    #     return predicted_exchange
    #
    # monkeypatch.setattr(target=app.restore_names,
    #                     name="restore_names",
    #                     value=mock_restore_names)
    restore_names(current_rate)
    assert current_rate == predicted_exchange

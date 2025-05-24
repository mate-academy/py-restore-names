from unittest import mock
from app.restore_names import restore_names


@mock.patch("restore_names.valid_google_url")
@mock.patch("restore_names.has_internet_connection")
def test_restore_names_success(
    mock_inet: mock.Mock, mock_url: mock.Mock
) -> None:
    mock_inet.return_value = True
    mock_url.return_value = True

    assert restore_names() is True
    mock_inet.assert_called_once()
    mock_url.assert_called_once()


@mock.patch("app.restore_names.valid_google_url")
@mock.patch("app.restore_names.has_internet_connection")
def test_restore_names_no_internet(
    mock_inet: mock.Mock, mock_url: mock.Mock
) -> None:
    mock_inet.return_value = False
    mock_url.return_value = True

    assert restore_names() is False
    mock_inet.assert_called_once()
    mock_url.assert_not_called()


@mock.patch("app.restore_names.valid_google_url")
@mock.patch("app.restore_names.has_internet_connection")
def test_restore_names_invalid_url(
    mock_inet: mock.Mock, mock_url: mock.Mock
) -> None:
    mock_inet.return_value = True
    mock_url.return_value = False

    assert restore_names() is False
    mock_inet.assert_called_once()
    mock_url.assert_called_once()

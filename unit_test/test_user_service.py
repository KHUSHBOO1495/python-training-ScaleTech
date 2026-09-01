from unittest.mock import patch, Mock

from user_service import get_user_name, create_greeting


@patch("user_service.requests.get")
def test_get_user_name(mock_get):
    fake_response = Mock()

    fake_response.json.return_value = {
        "name": "Alice"
    }

    mock_get.return_value = fake_response

    result = get_user_name(1)

    assert result == "Alice"


@patch("user_service.requests.get")
def test_create_greeting(mock_get):
    fake_response = Mock()

    fake_response.json.return_value = {
        "name": "Alice"
    }

    mock_get.return_value = fake_response

    result = create_greeting(1)

    assert result == "Hello, Alice!"

import json
from unittest.mock import MagicMock, patch

import pytest

from src.smac_fastapi_auth.automation.sec_mgr_helper import SecretsManagerHelper
from src.smac_fastapi_auth.automation.settings import (
    AutomationPrincipalSettings,
    SecretsManagerSettings,
)


@pytest.fixture
def mock_settings():
    return AutomationPrincipalSettings(
        secrets_manager=SecretsManagerSettings(
            profile="default", region="us-west-2", common_prefix="myapp"
        )
    )


@pytest.fixture
def mock_boto_session():
    with patch("boto3.Session") as mock:
        yield mock


@pytest.mark.usefixtures("mock_boto_session")
def test_get_secret_data_success(mock_boto_session, mock_settings):
    # Mock the boto3 session and client
    mock_session_instance = mock_boto_session.return_value
    mock_client = MagicMock()
    mock_session_instance.client.return_value = mock_client

    secret_string = json.dumps({"id": "service_123", "token": "token_abc"})
    mock_client.get_secret_value.return_value = {"SecretString": secret_string}

    helper = SecretsManagerHelper(settings=mock_settings)
    result = helper.get_secret_data("service_123")

    assert result.id == "service_123"
    assert result.token == "token_abc"
    mock_client.get_secret_value.assert_called_once_with(SecretId="myapp/service_123")


@pytest.mark.usefixtures("mock_boto_session")
def test_get_secret_data_no_secret_string(mock_boto_session, mock_settings):
    # Mock the boto3 session and client
    mock_session_instance = mock_boto_session.return_value
    mock_client = MagicMock()
    mock_session_instance.client.return_value = mock_client

    mock_client.get_secret_value.return_value = {}

    helper = SecretsManagerHelper(settings=mock_settings)

    with pytest.raises(ValueError, match="Secret is not having string data."):
        helper.get_secret_data("service_1234")

    mock_client.get_secret_value.assert_called_once_with(SecretId="myapp/service_1234")


@pytest.mark.usefixtures("mock_boto_session")
def test_get_secret_data_with_custom_prefix(mock_boto_session, mock_settings):
    # Mock the boto3 session and client
    mock_session_instance = mock_boto_session.return_value
    mock_client = MagicMock()
    mock_session_instance.client.return_value = mock_client

    secret_string = json.dumps({"id": "service_1235", "token": "token_abc"})
    mock_client.get_secret_value.return_value = {"SecretString": secret_string}

    mock_settings.secrets_manager.common_prefix = "myapp/"
    helper = SecretsManagerHelper(settings=mock_settings)
    result = helper.get_secret_data("service_1235")

    assert result.id == "service_1235"
    assert result.token == "token_abc"
    mock_client.get_secret_value.assert_called_once_with(SecretId="myapp/service_1235")

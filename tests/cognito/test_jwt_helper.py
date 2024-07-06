import asyncio
from unittest.mock import MagicMock, patch

import pytest
from aiohttp import ClientResponseError

from src.smac_fastapi_auth.cognito.jwt_helper import CognitoJwtHelper
from src.smac_fastapi_auth.cognito.settings import (
    ProviderCognitoSettings,
    UserPoolSettings,
    UserPoolsSettings,
)


@pytest.fixture
def mock_settings():
    return ProviderCognitoSettings(
        check_expiration=True,
        jwt_header_prefix="Bearer",
        jwt_header_name="Authorization",
        userpools=UserPoolsSettings(
            primary=UserPoolSettings(
                region="us-west-2",
                userpool_id="us-west-2_123456789",
                app_client_id="clientid12345",
                domain="https://example.com",
            )
        ),
    )


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.get")
async def test_get_principal_info_success(mock_get, mock_settings):
    mock_response = MagicMock()
    mock_response.status = 200
    mock_response.json = MagicMock(return_value=asyncio.Future())
    mock_response.json.return_value.set_result(
        {"sub": "1234567890", "email": "user@example.com"}
    )

    mock_get.return_value.__aenter__.return_value = mock_response

    helper = CognitoJwtHelper(settings=mock_settings)
    auth_header_value = "Bearer token"

    result = await helper.get_principal_info(auth_header_value)

    assert result == {"sub": "1234567890", "email": "user@example.com"}
    mock_get.assert_called_once()
    mock_response.raise_for_status.assert_called_once()
    mock_response.json.assert_called_once()


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.get")
async def test_get_principal_info_failure(mock_get, mock_settings):
    mock_get.return_value.__aenter__.side_effect = ClientResponseError(
        request_info=None,
        history=None,
        status=401,
        message="Unauthorized",
        headers=None,
    )

    helper = CognitoJwtHelper(settings=mock_settings)
    auth_header_value = "Bearer invalid_token"

    with pytest.raises(ClientResponseError):
        await helper.get_principal_info(auth_header_value)

    mock_get.assert_called_once()

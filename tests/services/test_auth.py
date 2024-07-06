from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException
from smac_fastapi_auth.cognito.settings import (
    ProviderCognitoSettings,
    UserPoolSettings,
    UserPoolsSettings,
)
from smac_fastapi_auth.core.constants import (
    ERROR_CODE_AUTH_ENFORCED_BUT_NOT_CONFIGURED,
    ERROR_CODE_AUTH_ENFORCED_PROVIDER_NOT_SUPPORTED,
)
from smac_fastapi_auth.core.settings import AuthProvider, AuthSettings
from smac_fastapi_auth.models.principal import PrincipalType
from smac_fastapi_auth.services.auth import (
    AuthenticationService,
)
from starlette.requests import Request


@pytest.fixture
def mock_settings():
    return AuthSettings(
        user_id="sub",
        provider=AuthProvider.cognito,
        provider_cognito=ProviderCognitoSettings(
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
        ),
    )


@pytest.mark.asyncio
async def test_enforce_no_provider(mock_settings):
    mock_settings.provider = AuthProvider.none
    service = AuthenticationService(settings=mock_settings)
    request = MagicMock(spec=Request)

    with pytest.raises(HTTPException) as exc_info:
        await service.enforce(request)

    assert exc_info.value.status_code == 500
    assert (
        f"Internal server error (Code: {ERROR_CODE_AUTH_ENFORCED_BUT_NOT_CONFIGURED})"
        in exc_info.value.detail
    )


@pytest.mark.asyncio
async def test_enforce_unsupported_provider(mock_settings):
    mock_settings.provider = "UNSUPPORTED_PROVIDER"
    service = AuthenticationService(settings=mock_settings)
    request = MagicMock(spec=Request)

    with pytest.raises(HTTPException) as exc_info:
        await service.enforce(request)

    assert exc_info.value.status_code == 500
    assert (
        f"Internal server error (Code: {ERROR_CODE_AUTH_ENFORCED_PROVIDER_NOT_SUPPORTED})"
        in exc_info.value.detail
    )


@pytest.mark.asyncio
@patch("smac_fastapi_auth.services.auth.CognitoAuth")
@patch("smac_fastapi_auth.services.auth.CognitoJwtHelper")
async def test_enforce_cognito_success(
    mock_cognito_jwt_helper_class, mock_cognito_auth_class, mock_settings
):
    mock_cognito_auth_instance = mock_cognito_auth_class.return_value
    mock_cognito_auth_instance.auth_required = AsyncMock()
    mock_cognito_jwt_helper_instance = mock_cognito_jwt_helper_class.return_value
    mock_cognito_jwt_helper_instance.get_principal_info = AsyncMock(
        return_value={"sub": "1234567890", "email": "user@example.com"}
    )

    service = AuthenticationService(settings=mock_settings)
    request = MagicMock(spec=Request)
    request.headers.get = MagicMock(return_value="Bearer token")

    result = await service.enforce(request)

    assert result.principal.id == "1234567890"
    assert result.principal.principal_type == PrincipalType.User
    mock_cognito_auth_instance.auth_required.assert_called_once_with(request)
    mock_cognito_jwt_helper_instance.get_principal_info.assert_called_once_with(
        "Bearer token"
    )


@pytest.mark.asyncio
@patch("smac_fastapi_auth.services.auth.CognitoAuth")
@patch("smac_fastapi_auth.services.auth.CognitoJwtHelper")
async def test_enforce_cognito_unauthorized(
    mock_cognito_jwt_helper_class, mock_cognito_auth_class, mock_settings
):
    mock_cognito_auth_instance = mock_cognito_auth_class.return_value
    mock_cognito_auth_instance.auth_required = AsyncMock()
    mock_cognito_jwt_helper_instance = mock_cognito_jwt_helper_class.return_value
    mock_cognito_jwt_helper_instance.get_principal_info = AsyncMock(
        side_effect=Exception("Unauthorized")
    )

    service = AuthenticationService(settings=mock_settings)
    request = MagicMock(spec=Request)
    request.headers.get = MagicMock(return_value="Bearer invalid_token")

    with pytest.raises(HTTPException) as exc_info:
        await service.enforce(request)

    assert exc_info.value.status_code == 401
    assert "Unauthorized" in exc_info.value.detail
    mock_cognito_auth_instance.auth_required.assert_called_once_with(request)
    mock_cognito_jwt_helper_instance.get_principal_info.assert_called_once_with(
        "Bearer invalid_token"
    )


@pytest.mark.asyncio
@patch("smac_fastapi_auth.services.auth.CognitoAuth")
@patch("smac_fastapi_auth.services.auth.CognitoJwtHelper")
async def test_enforce_cognito_missing_principal_id(
    mock_cognito_jwt_helper_class, mock_cognito_auth_class, mock_settings
):
    mock_cognito_auth_instance = mock_cognito_auth_class.return_value
    mock_cognito_auth_instance.auth_required = AsyncMock()
    mock_cognito_jwt_helper_instance = mock_cognito_jwt_helper_class.return_value
    mock_cognito_jwt_helper_instance.get_principal_info = AsyncMock(
        return_value={"email": "user@example.com"}
    )

    service = AuthenticationService(settings=mock_settings)
    request = MagicMock(spec=Request)
    request.headers.get = MagicMock(return_value="Bearer token")

    with pytest.raises(HTTPException) as exc_info:
        await service.enforce(request)

    assert exc_info.value.status_code == 401
    assert "Unauthorized" in exc_info.value.detail
    mock_cognito_auth_instance.auth_required.assert_called_once_with(request)
    mock_cognito_jwt_helper_instance.get_principal_info.assert_called_once_with(
        "Bearer token"
    )

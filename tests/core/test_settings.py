import pytest
from pydantic import ValidationError
from smac_fastapi_auth.core.settings import AuthProvider, AuthSettings

# from smac_fastapi_auth.cognito.settings import ProviderCognitoSettings, UserPoolsSettings, UserPoolSettings


def test_auth_settings_default(monkeypatch):
    monkeypatch.setenv("SMAC__AUTH__USER_ID", "username")
    monkeypatch.setenv("SMAC__AUTH__PROVIDER", "NONE")

    settings = AuthSettings()

    assert settings.user_id == "username"
    assert settings.provider == AuthProvider.none
    assert settings.provider_cognito is None


def test_auth_settings_cognito(monkeypatch):
    monkeypatch.setenv("SMAC__AUTH__USER_ID", "username")
    monkeypatch.setenv("SMAC__AUTH__PROVIDER", "COGNITO")
    monkeypatch.setenv("SMAC__AUTH__PROVIDER_COGNITO__CHECK_EXPIRATION", "False")
    monkeypatch.setenv("SMAC__AUTH__PROVIDER_COGNITO__JWT_HEADER_PREFIX", "JWT")
    monkeypatch.setenv("SMAC__AUTH__PROVIDER_COGNITO__JWT_HEADER_NAME", "Auth")
    monkeypatch.setenv(
        "SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__PRIMARY__REGION", "us-west-2"
    )
    monkeypatch.setenv(
        "SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__PRIMARY__USERPOOL_ID",
        "us-west-2_123456789",
    )
    monkeypatch.setenv(
        "SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__PRIMARY__APP_CLIENT_ID",
        "clientid12345",
    )
    monkeypatch.setenv(
        "SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__PRIMARY__DOMAIN",
        "https://example.com",
    )

    settings = AuthSettings()

    assert settings.user_id == "username"
    assert settings.provider == AuthProvider.cognito
    assert settings.provider_cognito is not None
    assert settings.provider_cognito.check_expiration is False
    assert settings.provider_cognito.jwt_header_prefix == "JWT"
    assert settings.provider_cognito.jwt_header_name == "Auth"
    assert settings.provider_cognito.userpools.primary.region == "us-west-2"
    assert (
        settings.provider_cognito.userpools.primary.userpool_id == "us-west-2_123456789"
    )
    assert settings.provider_cognito.userpools.primary.app_client_id == "clientid12345"
    assert (
        str(settings.provider_cognito.userpools.primary.domain)
        == "https://example.com/"
    )


def test_invalid_auth_provider(monkeypatch):
    monkeypatch.setenv("SMAC__AUTH__PROVIDER", "INVALID_PROVIDER")

    with pytest.raises(ValidationError):
        AuthSettings()


def test_missing_cognito_settings(monkeypatch):
    monkeypatch.setenv("SMAC__AUTH__USER_ID", "username")
    monkeypatch.setenv("SMAC__AUTH__PROVIDER", "COGNITO")

    with pytest.raises(
        ValueError,
        match="The provider is set to COGNITO, but the settings for Cognito are not provided.",
    ):
        AuthSettings()


def test_automation_principal_settings_with_default_header_names(monkeypatch):
    monkeypatch.setenv("SMAC__AUTH__USER_ID", "username")
    monkeypatch.setenv("SMAC__AUTH__PROVIDER", "NONE")
    monkeypatch.setenv(
        "SMAC__AUTH__AUTOMATION_PRINCIPALS__SECRETS_MANAGER__REGION", "eu-west-1"
    )
    monkeypatch.setenv(
        "SMAC__AUTH__AUTOMATION_PRINCIPALS__SECRETS_MANAGER__PROFILE", "fake"
    )
    monkeypatch.setenv(
        "SMAC__AUTH__AUTOMATION_PRINCIPALS__SECRETS_MANAGER__COMMON_PREFIX",
        "test/demo",
    )

    settings = AuthSettings()

    assert settings.automation_principals.secrets_manager.region == "eu-west-1"
    assert settings.automation_principals.secrets_manager.profile == "fake"
    assert settings.automation_principals.secrets_manager.common_prefix == "test/demo"
    assert settings.automation_principals.id_header_name == "SMAC-Principal"
    assert settings.automation_principals.token_header_name == "SMAC-Token"


def test_automation_principal_settings_with_custom_header_names(monkeypatch):
    monkeypatch.setenv("SMAC__AUTH__USER_ID", "username")
    monkeypatch.setenv("SMAC__AUTH__PROVIDER", "NONE")
    monkeypatch.setenv(
        "SMAC__AUTH__AUTOMATION_PRINCIPALS__SECRETS_MANAGER__REGION", "eu-west-1"
    )
    monkeypatch.setenv(
        "SMAC__AUTH__AUTOMATION_PRINCIPALS__SECRETS_MANAGER__PROFILE", "fake"
    )
    monkeypatch.setenv(
        "SMAC__AUTH__AUTOMATION_PRINCIPALS__SECRETS_MANAGER__COMMON_PREFIX",
        "test/demo",
    )
    monkeypatch.setenv(
        "SMAC__AUTH__AUTOMATION_PRINCIPALS__ID_HEADER_NAME", "CUSTOM-Principal"
    )
    monkeypatch.setenv(
        "SMAC__AUTH__AUTOMATION_PRINCIPALS__TOKEN_HEADER_NAME", "CUSTOM-Token"
    )

    settings = AuthSettings()

    assert settings.automation_principals.secrets_manager.region == "eu-west-1"
    assert settings.automation_principals.secrets_manager.profile == "fake"
    assert settings.automation_principals.secrets_manager.common_prefix == "test/demo"
    assert settings.automation_principals.id_header_name == "CUSTOM-Principal"
    assert settings.automation_principals.token_header_name == "CUSTOM-Token"

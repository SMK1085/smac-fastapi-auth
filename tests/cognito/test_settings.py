from smac_fastapi_auth.cognito.settings import (
    ProviderCognitoSettings,
    UserPoolSettings,
    UserPoolsSettings,
)


def test_serialization_with_secondary_userpool():
    settings = ProviderCognitoSettings(
        check_expiration=True,
        jwt_header_prefix="Bearer",
        jwt_header_name="Authorization",
        userpools=UserPoolsSettings(
            primary=UserPoolSettings(
                region="us-east-1",
                userpool_id="us-east-1_123456789",
                app_client_id="clientid12345",
                domain="https://example.com",
            ),
            secondary=UserPoolSettings(
                region="us-west-2",
                userpool_id="us-west-2_987654321",
                app_client_id="clientid54321",
                domain="https://example2.com",
            ),
        ),
    )

    assert settings.model_dump() == {
        "check_expiration": True,
        "jwt_header_prefix": "Bearer",
        "jwt_header_name": "Authorization",
        "userpools": {
            "primary": {
                "region": "us-east-1",
                "userpool_id": "us-east-1_123456789",
                "app_client_id": "clientid12345",
                "domain": "https://example.com",
            },
            "secondary": {
                "region": "us-west-2",
                "userpool_id": "us-west-2_987654321",
                "app_client_id": "clientid54321",
                "domain": "https://example2.com",
            },
        },
    }

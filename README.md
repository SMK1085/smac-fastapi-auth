# SMAC: FastAPI Auth

![GitHub Workflow](https://github.com/SMK1085/smac-fastapi-auth/actions/workflows/main.yaml/badge.svg)

This project contains the reusable code for authentication in Python backends using FastAPI.
It leverages Cognito User Pools and Secrets Manager for authentication.

## Usage

TBD

### Authentication of Service Principals (Automation)

The authentication of service principals is done leveraging AWS Secrets Manager. The service principal needs to provide a token that and an identifier.
The name identifier is used to retrieve the secret from Secrets Manager. The token is validated against the secret.
The secret in Secrets Manager needs to be a JSON object with the following structure:

```json
{
  "token": "Secret Token",
  "id": "Actual principal identifier of the service"
}
```

### Configuration (Environment Variables)

Configuration is done through environment variables. The following table lists the environment variables that can be used to configure the authentication.

| Variable | Description | Default |
|----------|-------------|---------|
| `SMAC__AUTH__USER_ID` | The claim name which contains the unique user identifier. | `email` |
| `SMAC__AUTH__PROVIDER` | The provider name. | `NONE` |
| `SMAC__AUTH__PROVIDER_COGNITO__CHECK_EXPIRATION` | Whether to check the expiration of the token. | `True` |
| `SMAC__AUTH__PROVIDER_COGNITO__JWT_HEADER_PREFIX` | The prefix for the JWT header. | `Bearer` |
| `SMAC__AUTH__PROVIDER_COGNITO__JWT_HEADER_NAME` | The name of the JWT header. | `Authorization` |
| `SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__PRIMARY__REGION` | The region of the primary user pool. | `None` |
| `SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__PRIMARY__USERPOOL_ID` | The ID of the primary user pool. | `None` |
| `SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__PRIMARY__APP_CLIENT_ID` | The app client ID of the primary user pool. | `None` |
| `SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__PRIMARY__DOMAIN` | The domain name of the primary user pool. | `None` |
| `SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__SECONDARY__REGION` | The region of the secondary user pool. | `None` |
| `SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__SECONDARY__USERPOOL_ID` | The ID of the secondary user pool. | `None` |
| `SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__SECONDARY__APP_CLIENT_ID` | The app client ID of the secondary user pool. | `None` |
| `SMAC__AUTH__PROVIDER_COGNITO__USERPOOLS__SECONDARY__DOMAIN` | The domain name of the secondary user pool. | `None` |
| `SMAC__AUTH__AUTOMATION_PRINCIPALS__SECRETS_MANAGER__REGION` | The region of the Secrets Manager. | `None` |
| `SMAC__AUTH__AUTOMATION_PRINCIPALS__SECRETS_MANAGER__PROFILE` | The AWS credentials profile to authenticate with. | `None` |
| `SMAC__AUTH__AUTOMATION_PRINCIPALS__SECRETS_MANAGER__COMMON_PREFIX` | The common prefix for the secrets in the Secrets Manager. | `""` |
| `SMAC__AUTH__AUTOMATION_PRINCIPALS__ID_HEADER_NAME` | The name of the header containing the automation principal name. | `SMAC-Principal` |
| `SMAC__AUTH__AUTOMATION_PRINCIPALS__TOKEN_HEADER_NAME` | The name of the header containing the automation principal token. | `SMAC-Token` |

Note: The secondary user pool is entirely optional. If it is configured, keep in mind that the `SMAC__AUTH__USER_ID` cannot be set to `sub` as the user pools create the sub claim automatically. It is advised to use the email address as the user identifier in this case so that the application logic does not need to differentiate between the primary and secondary user pools.

## Development

### Setup

1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Install dependencies:

    ```bash
    poetry config virtualenvs.in-project true
    poetry install --with dev

    # Install pre-commit hooks
    poetry run pre-commit install
    ```

3. Run tests:

    ```bash
    poetry run pytest --cov .
    ```

## Releases

Releases are done automatically using [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/commit-parsing.html).

Refer to the [CHANGELOG](CHANGELOG.md) for the release history.

Note that minor releases are done, if the underlying fastapi version changes. This is to ensure that the package is compatible with the latest fastapi version and to address any security vulnerabilities.

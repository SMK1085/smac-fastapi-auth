import pytest
from pydantic import ValidationError

from src.smac_fastapi_auth.models import AuthenticatedPrincipal, PrincipalType


def test_authenticated_principal_valid_user():
    principal = AuthenticatedPrincipal(id="12345", principal_type=PrincipalType.User)

    assert principal.id == "12345"
    assert principal.principal_type == PrincipalType.User


def test_authenticated_principal_valid_service():
    principal = AuthenticatedPrincipal(
        id="service_001", principal_type=PrincipalType.Service
    )

    assert principal.id == "service_001"
    assert principal.principal_type == PrincipalType.Service


def test_authenticated_principal_missing_id():
    with pytest.raises(ValidationError) as exc_info:
        AuthenticatedPrincipal(principal_type=PrincipalType.User)

    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("id",)
    assert errors[0]["msg"] == "Field required"
    assert errors[0]["type"] == "missing"


def test_authenticated_principal_missing_principal_type():
    with pytest.raises(ValidationError) as exc_info:
        AuthenticatedPrincipal(id="12345")

    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("principal_type",)
    assert errors[0]["msg"] == "Field required"
    assert errors[0]["type"] == "missing"


def test_authenticated_principal_invalid_principal_type():
    with pytest.raises(ValidationError) as exc_info:
        AuthenticatedPrincipal(id="12345", principal_type="invalid_type")

    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("principal_type",)
    assert "Input should be 'user', 'service' or 'anonymous" in errors[0]["msg"]
    assert errors[0]["type"] == "enum"

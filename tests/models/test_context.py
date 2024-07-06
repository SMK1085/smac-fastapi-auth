import pytest
from pydantic import ValidationError

from src.smac_fastapi_auth.models import (
    AuthenticatedContext,
    AuthenticatedPrincipal,
    PrincipalType,
)


def test_authenticated_context_valid_user():
    principal = AuthenticatedPrincipal(id="12345", principal_type=PrincipalType.User)
    context = AuthenticatedContext(principal=principal)

    assert context.principal == principal
    assert context.principal.id == "12345"
    assert context.principal.principal_type == PrincipalType.User


def test_authenticated_context_valid_service():
    principal = AuthenticatedPrincipal(
        id="service_001", principal_type=PrincipalType.Service
    )
    context = AuthenticatedContext(principal=principal)

    assert context.principal == principal
    assert context.principal.id == "service_001"
    assert context.principal.principal_type == PrincipalType.Service


def test_authenticated_context_missing_principal():
    with pytest.raises(ValidationError) as exc_info:
        AuthenticatedContext()

    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("principal",)
    assert errors[0]["msg"] == "Field required"
    assert errors[0]["type"] == "missing"


def test_authenticated_context_invalid_principal():
    with pytest.raises(ValidationError) as exc_info:
        AuthenticatedContext(
            principal={"id": "12345", "principal_type": "invalid_type"}
        )

    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("principal", "principal_type")
    assert "Input should be 'user', 'service' or 'anonymous" in errors[0]["msg"]
    assert errors[0]["type"] == "enum"

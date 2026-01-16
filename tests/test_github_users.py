import os
import pytest
import requests

from src.api_client import APIClient

# Smoke tests for GitHub public user endpoints


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("username", ["octocat", "defunkt", "mojombo"])
def test_get_user_by_username(api_client, username):
    """
    Smoke test:
    Verify that GitHub public user endpoint (/users/{username})
    is reachable and returns a valid user object structure.
    """
    response = api_client.get(f"/users/{username}")

    assert response.status_code == 200

    data = response.json()
    assert data["login"].lower() == username.lower()
    assert "id" in data
    assert "html_url" in data
    assert data["type"] in {"User", "Organization"}


@pytest.mark.negative
def test_unauthorized_request_returns_401():
    """
    Verify GitHub API returns 401 when accessing an endpoint that requires auth
    without providing a token.
    """
    session = requests.Session()
    base_url = os.getenv("API_BASE_URL", "https://api.github.com").rstrip("/")
    client = APIClient(base_url=base_url, session=session)

    response = client.get("/user")

    assert response.status_code == 401
    data = response.json()
    assert "message" in data    

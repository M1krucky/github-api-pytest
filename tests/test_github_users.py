import pytest

# Smoke tests for GitHub public user endpoints


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.parametrize("username", ["octocat"])
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

import pytest

# Smoke tests for GitHub API availability and basic rate limit contract


@pytest.mark.smoke
@pytest.mark.positive
def test_rate_limit(api_client):
    """
    Smoke test:
    Verify GitHub /rate_limit endpoint is reachable
    and returns the expected response structure.
    """
    response = api_client.get("/rate_limit")

    assert response.status_code == 200

    data = response.json()
    assert "resources" in data
    assert "core" in data["resources"]
    assert "rate" in data

import pytest

# Tests for GitHub repository endpoints


@pytest.mark.smoke
@pytest.mark.positive
def test_get_repo_by_owner_and_name(api_client):
    """
    Smoke test:
    Verify GitHub repo endpoint (/repos/{owner}/{repo}) is reachable
    and returns a valid repository object structure.
    """
    owner = "octocat"
    repo = "Hello-World"

    response = api_client.get(f"/repos/{owner}/{repo}")

    assert response.status_code == 200

    data = response.json()
    assert data["name"] == repo
    assert data["full_name"].lower() == f"{owner}/{repo}".lower()
    assert "owner" in data and "login" in data["owner"]
    assert data["owner"]["login"].lower() == owner.lower()
    assert "html_url" in data


@pytest.mark.negative
@pytest.mark.parametrize(
    "owner, repo",
    [
        ("octocat", "this-repo-should-not-exist-123456789"),
        ("octocat", "definitely-not-a-repo-000000000"),
        ("this-owner-should-not-exist-123456789", "some-repo"),
    ],
)
def test_get_repo_returns_404_for_non_existing_repo(api_client, owner, repo):
    """
    Negative test:
    Verify GitHub returns 404 for a repository that does not exist.
    """
    response = api_client.get(f"/repos/{owner}/{repo}")

    assert response.status_code == 404




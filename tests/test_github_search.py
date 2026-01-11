import pytest

# Tests for GitHub repository search functionality


@pytest.mark.positive
def test_search_repositories_by_keyword(api_client):
    """
    Verify GitHub repository search endpoint returns
    a list of repositories for a given keyword.
    """
    params = {"q": "pytest"}

    response = api_client.get("/search/repositories", params=params)

    assert response.status_code == 200

    data = response.json()
    assert "total_count" in data
    assert "items" in data
    assert isinstance(data["items"], list)
    assert len(data["items"]) > 0

    names = [repo["name"].lower() for repo in data["items"]]
    assert any("pytest" in name for name in names)

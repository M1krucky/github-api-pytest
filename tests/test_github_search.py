import pytest

# Tests for GitHub repository search functionality


@pytest.mark.positive
@pytest.mark.parametrize("keyword", ["pytest", "requests", "selenium"])
def test_search_repositories_by_keyword(api_client, keyword):
    """
    Verify GitHub repository search endpoint returns
    a list of repositories for a given keyword.
    """
    params = {"q": keyword}

    response = api_client.get("/search/repositories", params=params)

    assert response.status_code == 200

    data = response.json()
    assert "total_count" in data
    assert "items" in data
    assert isinstance(data["items"], list)
    assert len(data["items"]) > 0

    names = [repo["name"].lower() for repo in data["items"]]
    assert any(keyword.lower() in name for name in names)


@pytest.mark.negative
def test_search_repositories_with_empty_query_returns_422(api_client):
    """
    Verify GitHub search API returns 422 when query parameter is missing or empty.
    """
    response = api_client.get("/search/repositories", params={"q": ""})

    assert response.status_code == 422

    data = response.json()
    assert "message" in data


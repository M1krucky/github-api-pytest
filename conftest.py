import pytest
import requests
from src.api_client import APIClient
import os

# PyTest configuration and shared fixtures for GitHub API testing.
# This file defines environment-based API setup (base URL, auth headers),
# a shared HTTP session, and the API client used by all tests.


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("API_BASE_URL", "https://api.github.com").rstrip("/") 


@pytest.fixture(scope="session")
def default_headers():
    headers = {"Accept": "application/vnd.github+json"}

    token = os.getenv("GITHUB_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers 
 

@pytest.fixture(scope="session")
def http_session(default_headers):
    s = requests.Session()
    s.headers.update(default_headers)
    return s


@pytest.fixture(scope="session")
def api_client(base_url, http_session):
    return APIClient(base_url=base_url, session=http_session, timeout=10)


@pytest.fixture(scope="session")
def api_token():
    return os.getenv("API_TOKEN")

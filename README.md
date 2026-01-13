## GitHub API PyTest Automation

### Portfolio-style API test automation framework built with Python + PyTest + requests using the real GitHub REST API (no mock services). 

#### What’s included (current):

- API client wrapper (src/api_client.py) with shared requests.Session, base URL, and timeout
- Config via environment variables:
  - API_BASE_URL (default: https://api.github.com)
  - GITHUB_TOKEN (optional; enables authenticated mode)
- PyTest suite covering core GitHub endpoints:
  - GET /rate_limit
  - GET /users/{username}
  - GET /repos/{owner}/{repo} (+ 404 negative test)
  - GET /search/repositories (query params + basic business validation)
- Markers configured in pytest.ini: smoke, positive, negative

#### How to run:

1. Create and activate a virtual environment
2. Install dependencies:
   pip install -r requirements.txt

3. (Optional) Set token to increase rate limits:
   export GITHUB_TOKEN="your_token_here"

4. Run tests:
   pytest -q

### Roadmap (next pushes):

- Expand negative coverage (auth errors, not-found, validation errors)
- Add parametrization for scalable endpoint coverage
- Add reporting (HTML/JUnit) and CI workflow (GitHub Actions)
- Improve assertions around response schema and business rules

  <!-- CI registration -->
   


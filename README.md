## GitHub API QA Automation (PyTest)

![CI](https://github.com/M1krucky/github-api-qa-pytest/actions/workflows/ci.yml/badge.svg)

Professional API test automation framework built with **Python**, **PyTest**, and **requests** against the **real GitHub REST API** (no mock services).  
Designed as a **portfolio-grade QA Automation project** with CI, reporting, and real-world workflow.

---

### What is tested

The framework validates core GitHub API functionality and behavior.

**Endpoints**

- `GET /rate_limit`
- `GET /users/{username}`
- `GET /repos/{owner}/{repo}`
- `GET /search/repositories`

**Coverage**

- Positive scenarios (valid users, repositories, search queries)
- Negative scenarios (404 for non-existing repositories)
- Business rules (e.g. repository type, non-empty search results)
- Smoke tests for fast health checks

**Test organization**

- PyTest markers: `smoke`, `positive`, `negative`
- Parametrized tests for scalable coverage

---

### Tech stack

- Python 3.x
- PyTest
- requests
- pytest-html
- GitHub Actions (CI)

---

### Project structure

```
src/
    api_client.py

tests/
    test_github_users.py
    test_github_repos.py
    test_github_search.py

reports/
    junit.xml
    report.html

.github/workflows/
    ci.yml

```

---

### How authentication works

Environment variables:

- `API_BASE_URL` (default: `https://api.github.com`)
- `GITHUB_TOKEN` (optional; increases GitHub API rate limits)

If `GITHUB_TOKEN` is set, all requests are sent with:

```
Authorization: Bearer <token>

```

CI uses GitHub’s built-in `GITHUB_TOKEN` automatically.

---

### How to run locally

```bash
python -m venv .venv
source .venv/bin/activate      # or .venv\Scripts\activate on Windows

pip install -r requirements.txt
export GITHUB_TOKEN="your_token_here"   # optional

pytest -q

```

To generate reports locally:

```bash
pytest -q --junitxml=reports/junit.xml --html=reports/report.html --self-contained-html

```

---

### CI and test reports

Every push and pull request runs the full test suite in GitHub Actions.

The CI pipeline produces:

- JUnit XML report
- HTML test report

Both are uploaded as artifacts.

To view reports:

1. Open the Actions tab
2. Click the latest successful run
3. Download the test-reports artifact
4. Open report.html in a browser

---

### Why this project exists

This repository demonstrates:

- Real-world API test automation
- CI-driven quality gates
- Test reporting and traceability
- Professional Git and Pull-Request workflow

It is built to mirror how QA Automation Engineers work in production teams.

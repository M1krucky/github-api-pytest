from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests

# Lightweight API client used by tests to send HTTP requests to GitHub REST API.
# It centralizes base URL handling, shared session usage, and request timeouts. 


@dataclass(frozen=True)
class APIClient:
    """Thin wrapper over requests.Session to keep API calls consistent across tests."""
    base_url: str
    session: requests.Session
    timeout: int = 10

    def get(self, path: str, *, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.get(url, params=params, timeout=self.timeout)

    def post(self, path: str, *, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self.session.post(url, json=json, timeout=self.timeout)

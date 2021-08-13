import pytest
import requests

from quantel import Quantel, exceptions


def test_invalid_api_key():
    with pytest.raises(exceptions.InvalidAPIKey):
        qt = Quantel(api_key="000")
        goog = qt.ticker('goog')


class MockResponse:
    status_code = 503


def test_gateway_error(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    with pytest.raises(exceptions.GatewayError):
        qt = Quantel(api_key="000")
        goog = qt.ticker('goog')

import pytest
import requests

from quantel import Quantel, exceptions


def test_invalid_api_key():
    """
    Test 401, and 403 invalid API key errors.
    """
    with pytest.raises(exceptions.InvalidAPIKey):
        qt = Quantel(api_key="000")
        goog = qt.ticker('goog')


class MockGatewayResponse:
    status_code = 503


def test_gateway_error(monkeypatch):
    """
    Test 503 Gateway Error
    """

    def mock_get(*args, **kwargs):
        return MockGatewayResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    with pytest.raises(exceptions.GatewayError):
        qt = Quantel(api_key="000")
        goog = qt.ticker('goog')


class MockTooManyRequestsResponse:
    status_code = 429


class MockValidAPIKey:
    status_code = 200


@pytest.fixture()
def valid_api_key(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockValidAPIKey()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    qt = Quantel(api_key="000")
    goog = qt.ticker('goog')

    return goog


def test_too_many_requests_error(monkeypatch, valid_api_key):
    """
    Test 429 Too Many Requests error
    """

    def mock_get(*args, **kwargs):
        return MockTooManyRequestsResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests.Session, "get", mock_get)

    with pytest.raises(exceptions.TooManyRequests):

        goog = valid_api_key

        print(goog.profile())

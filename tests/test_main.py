from flask import Flask
import pytest


def test_health_endpoint(client):
    response = client.get("/healthcheck")

    assert response.status_code == 200
    assert response.data == b"SERVER_IS_READ"

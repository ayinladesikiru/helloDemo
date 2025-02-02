from django.test import TestCase
from django.test.client import Client
import pytest


# Create your tests here.
@pytest.mark.django_db
def test_greeting():
    api_client = Client()
    response = api_client.post("/hello")
    assert response.status_code == 200

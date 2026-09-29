import pytest
from app.main import add, app

def test_add_positive():
  assert add(2, 3) == 5

def test_add_negative():
  assert add(-1, -1) == -2

def test_flask_hello():
  client = app.test_client()
  resp = client.get("/")
  assert resp.status_code == 200
  data = resp.get_json()
  assert data["message"].startswith("Hello")

def test_fail():
  assert add(2, 2) == 4
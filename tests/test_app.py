# Run the tests with: pytest tests/test_app.py
import app

def test_add_numbers():
    assert app.add_numbers(2, 3) == 5

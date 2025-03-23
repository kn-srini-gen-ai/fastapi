from fastapi.testclient import TestClient
from app.main import app  # Import the FastAPI app from your main file

# Create a TestClient instance
client = TestClient(app)

# Test Case 1: Add Two Numbers
def test_add_numbers():
    response = client.post("/add", json={"num1": 15.0, "num2": 3.0})
    assert response.status_code == 200
    assert response.json() == {"result": 18.0}

# Test Case 2: Multiply Two Numbers
def test_multiply_numbers():
    response = client.post("/multiply", json={"num1": 15.0, "num2": 3.0})
    assert response.status_code == 200
    assert response.json() == {"result": 45.0}

# Test Case 3: Add Two Numbers (Negative Inputs)
def test_add_negative_numbers():
    response = client.post("/add", json={"num1": -5.0, "num2": -3.0})
    assert response.status_code == 200
    assert response.json() == {"result": -8.0}

# Test Case 4: Multiply Two Numbers (Negative Inputs)
def test_multiply_negative_numbers():
    response = client.post("/multiply", json={"num1": -5.0, "num2": 3.0})
    assert response.status_code == 200
    assert response.json() == {"result": -15.0}

# Test Case 5: Add Two Numbers (Decimal Inputs)
def test_add_decimal_numbers():
    response = client.post("/add", json={"num1": 5.5, "num2": 3.2})
    assert response.status_code == 200
    assert response.json() == {"result": 8.7}

# Test Case 6: Multiply Two Numbers (Decimal Inputs)
def test_multiply_decimal_numbers():
    response = client.post("/multiply", json={"num1": 5.5, "num2": 3.2})
    assert response.status_code == 200
    assert response.json() == {"result": 17.6}

# Test Case 7: Invalid Input (Missing Field)
def test_add_missing_field():
    response = client.post("/add", json={"num1": 5.0})  # Missing num2
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "num2"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }

# Test Case 8: Invalid Input (Non-Numeric Input)
def test_multiply_non_numeric_input():
    response = client.post("/multiply", json={"num1": "five", "num2": 3.0})  # Invalid num1
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "num1"],
                "msg": "value is not a valid float",
                "type": "type_error.float",
            }
        ]
    }

# Test Case 9: Root Endpoint
def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI calculator!"}
import json
import pytest
from fastapi.testclient import TestClient

from api.main import app
 
@pytest.fixture
def input_data():
    # Load the input data from the JSON file
    with open('tests/input_data.json') as f:
        return json.load(f)  
 
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client
 
def test_statistics_api(client, input_data):
    # Send a POST request to /stats/ with the input data read from the file
    response = client.post(
        '/stats/', 
        json=input_data  
    )
    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    # Parse the JSON response
    result = response.json()
    # Assertions based on the expected behavior
    assert "meanval" in result
    assert "medianval" in result
    assert "IQR" in result
    assert "Lowerlimit" in result
    assert "upperlimit" in result
    assert "stdlimits" in result
    # Compare the returned values with the expected ones
    assert result["meanval"] == 85.76
    assert result["medianval"] == 89.5
    assert result["IQR"] == 38.25
    assert result["Lowerlimit"] == 9.875
    assert result["upperlimit"] == 162.875
    assert result["stdlimits"]["1_std_limits"] == [57.50433862037556, 114.01566137962445]
    assert result["stdlimits"]["2_std_limits"] == [29.248677240751128, 142.27132275924887]
    assert result["stdlimits"]["3_std_limits"] == [0.9930158611266933, 170.52698413887333]

def invalidinput_data():
    # Load the invalidinput data from the JSON file
    with open('tests/invalidinput_data.json') as d:
        return json.load(d)  
 
def test_invalid_data(client,invalidinput_data):
    # Send a POST request with invalid input (e.g., non-numeric data)
    response = client.post(
        '/stats/',
        json= invalidinput_data # Invalid data
    )
    # Check if the status code is 422 Unprocessable Entity (for invalid input)
    assert response.status_code == 422
    assert "details" in response.json()

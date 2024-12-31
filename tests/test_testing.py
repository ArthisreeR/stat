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
def wrong_data():
    with open('tests/invalidinput_data.txt') as a:
        return a.read()
 
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client
def test_stat_api(client, input_data):
    # Send a POST request to /stats/ with the input data read from the file
    response = client.post('/stats/', data = {"input" : input_data })
    assert response.status_code == 200
    result = response.json()
    # Assertions based on the expected behavior
    assert "meanval" in result
    assert "medianval" in result
    assert "IQR" in result
    assert "Lowerlimit" in result
    assert "upperlimit" in result
    assert "stdlimits" in result
    # Compare the returned values with the expected ones
    assert result["meanval"] == 55
    assert result["medianval"] == 55
    assert result["IQR"] == 55
    assert result["Lowerlimit"] == -55
    assert result["upperlimit"] == 165
    assert result["stdlimits"]["1_std_limits"] == [26.277186767309857,
      83.72281323269014]
    assert result["stdlimits"]["2_std_limits"] == [-2.445626465380286,
      112.44562646538029]
    assert result["stdlimits"]["3_std_limits"] == [-31.16843969807043,
      141.16843969807042]

def test_invalid_data(client, wrong_data):
    # Send a POST request with invalid input (e.g., non-numeric data)
    response = client.post( '/stats/',data = {"input" : wrong_data })  
    # Check if the status code is 422 Unprocessable Entity (for invalid input)
    assert response.status_code != 200
    assert "detail" in response.json()

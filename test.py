from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

data = {"text": "I am happy"}

response = client.post('http://localhost:8000/predict', json=data, headers={
    "Content-Type": "application/json"
})

print(response.status_code)
print(response.reason)
print(response.json())


from fastapi import FastAPI
from utilities import predict_pipeline
from json import loads
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:8000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

class Props(BaseModel):
    text: str

@app.post('/predict')
async def predict(request: Props):
    try:
        text = request.text
    except KeyError:
        return loads({'error': 'No text sent'})
    
    prediction = predict_pipeline(text)
    try:
        result = prediction
    except TypeError as e:
        result = {'error': str(e)}
    return result

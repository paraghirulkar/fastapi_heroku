import uvicorn
from fastapi import FastAPI
# import numpy as np 
# import pandas as pd 
# import pickle

app = FastAPI()

@app.get('/')
def home():
    return "Learning FastAPI"

if __name__ == '__main__':
    uvicorn.run(app)
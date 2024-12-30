import json
import datetime
import asyncio
 
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI,Form
from starlette.middleware.cors import CORSMiddleware
import pandas as pd
import os
import traceback
import ast
import re
from statparam import stat
 
app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (you can restrict this to specific domains)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (you can specify methods if needed)
    allow_headers=["*"],  # Allows all headers
)


@app.post("/stats/")
async def statfunction( input : str = Form(...)):
     json_data = ast.literal_eval(input)
     result = stat(json_data)
     return result
 
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8008)

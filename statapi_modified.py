from fastapi import FastAPI,Form
import json
import datetime
import asyncio
 
import uvicorn
import pandas as pd
import os
import traceback
import ast
import re
import statparam
from statparam import stat
 
app = FastAPI(debug=True)
@app.post("/stats/")
async def statfunction( input : str = Form(...)):
     json_data = ast.literal_eval(input)
     result = stat(json_data)
     return result
 
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8007)
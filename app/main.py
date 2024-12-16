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
from app.statparam import stat
 
app = FastAPI(debug=True)
@app.post("/stats/")
async def statfunction( input : str = Form(...)):
   try:
       json_data = ast.literal_eval(input)
       result = stat(json_data)
       return result
   except Exception as e:
       return {"error": str(e)}
      
 
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8007)

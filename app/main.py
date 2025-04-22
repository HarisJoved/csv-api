from fastapi import FastAPI, File, UploadFile
import pandas as pd
import json
import io

app = FastAPI()

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    # Read the uploaded file
    contents = await file.read()
    # Convert the file contents to a pandas DataFrame
    df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
    # Calculate statistics
    stats = {
        'columns': list(df.columns),
        'row_count': len(df),
        'column_stats': df.describe().to_dict()
    }
    # Return the statistics as JSON
    return json.dumps(stats)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the CSV Stats API! Use POST /upload-csv/ to upload a CSV file."}

@app.put("/update-config/")
async def update_config(config: dict):
    # For demonstration, just return the received config
    return {"updated_config": config} 
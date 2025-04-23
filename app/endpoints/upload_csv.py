from fastapi import UploadFile, Depends
import pandas as pd
import io
import json
from app.auth import get_current_user

async def upload_csv(file: UploadFile, current_user: dict = Depends(get_current_user)):
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
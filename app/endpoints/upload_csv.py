from fastapi import UploadFile, Depends, HTTPException, status, File
import pandas as pd
import io
from app.auth import get_current_user
from app.models.csv_stats import CSVStatistics
from app.models.common import ErrorResponse

async def upload_csv(file: UploadFile = File(...), current_user: dict = Depends(get_current_user)):
    """
    Upload a CSV file and get statistics about its contents.
    
    The endpoint requires authentication.
    """
    # Check file extension
    if not file.filename.endswith('.csv'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only CSV files are allowed"
        )
    
    try:
        # Read the uploaded file
        contents = await file.read()
        
        # Convert the file contents to a pandas DataFrame
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        
        # Calculate statistics
        stats = CSVStatistics(
            columns=list(df.columns),
            row_count=len(df),
            column_stats=df.describe().to_dict(),
            file_name=file.filename
        )
        
        return stats
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing CSV file: {str(e)}"
        ) 
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class CSVStatistics(BaseModel):
    """Model for CSV file statistics response."""
    columns: List[str] = Field(..., description="List of column names in the CSV")
    row_count: int = Field(..., description="Number of rows in the CSV")
    column_stats: Dict[str, Dict[str, Any]] = Field(..., description="Statistical information for each column")
    file_name: Optional[str] = Field(None, description="Name of the uploaded CSV file")
    
    class Config:
        json_schema_extra = {
            "example": {
                "columns": ["id", "name", "age", "salary"],
                "row_count": 100,
                "column_stats": {
                    "id": {
                        "count": 100.0,
                        "mean": 50.5,
                        "std": 29.01,
                        "min": 1.0,
                        "25%": 25.75,
                        "50%": 50.5,
                        "75%": 75.25,
                        "max": 100.0
                    },
                    "age": {
                        "count": 100.0,
                        "mean": 35.6,
                        "std": 10.2,
                        "min": 21.0,
                        "25%": 28.0,
                        "50%": 35.0,
                        "75%": 42.0,
                        "max": 65.0
                    }
                },
                "file_name": "employee_data.csv"
            }
        } 
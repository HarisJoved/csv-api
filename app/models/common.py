from pydantic import BaseModel, Field
from typing import Optional, Any

class BaseResponse(BaseModel):
    """Base model for all API responses."""
    status: str = Field(..., description="Status of the request: success or error")
    message: str = Field(..., description="Message describing the result")

class SuccessResponse(BaseResponse):
    """Model for successful responses."""
    status: str = Field("success", description="Success status")
    data: Optional[Any] = Field(None, description="Response data")
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Welcome to the CSV Stats API!",
                "data": {
                    "endpoints": {
                        "/": "Root endpoint with API information (GET)",
                        "/upload-csv/": "Upload and analyze CSV files (POST, requires auth)",
                        "/update-config/": "Update configuration settings (PUT, requires auth)"
                    },
                    "api_version": "1.0.0",
                    "documentation": "/docs"
                }
            }
        }

class ErrorResponse(BaseResponse):
    """Model for error responses."""
    status: str = Field("error", description="Error status")
    error_code: Optional[str] = Field(None, description="Error code")
    details: Optional[Any] = Field(None, description="Additional error details") 
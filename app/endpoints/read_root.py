from app.models.common import SuccessResponse

async def read_root():
    """
    Get welcome message and API information.
    
    This endpoint does not require authentication.
    """
    return SuccessResponse(
        message="Welcome to the CSV Stats API!",
        data={
            "endpoints": {
                "/": "Root endpoint with API information (GET)",
                "/upload-csv/": "Upload and analyze CSV files (POST, requires auth)",
                "/update-config/": "Update configuration settings (PUT, requires auth)"
            },
            "api_version": "1.0.0",
            "documentation": "/docs"
        }
    ) 
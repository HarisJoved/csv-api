from fastapi import FastAPI, File, HTTPException
from app.endpoints.upload_csv import upload_csv
from app.endpoints.read_root import read_root
from app.endpoints.update_config import update_config
from fastapi.exceptions import RequestValidationError
from app.error_handlers import http_exception_handler, validation_exception_handler
from app.models.csv_stats import CSVStatistics
from app.models.config import ConfigResponse, ConfigRequest
from app.models.common import SuccessResponse

# Create FastAPI application
app = FastAPI(
    title="CSV Statistics API",
    description="API for analyzing CSV files and returning statistical information",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Register routes with response models
app.get("/", response_model=SuccessResponse)(read_root)
app.post("/upload-csv/", response_model=CSVStatistics)(upload_csv)
app.put("/update-config/", response_model=ConfigResponse)(update_config)

# Register exception handlers
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler) 
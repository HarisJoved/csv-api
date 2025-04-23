from fastapi import FastAPI, File, HTTPException
from app.endpoints.upload_csv import upload_csv
from app.endpoints.read_root import read_root
from app.endpoints.update_config import update_config
from fastapi.exceptions import RequestValidationError
from app.error_handlers import http_exception_handler, validation_exception_handler

app = FastAPI()

app.post("/upload-csv/")(upload_csv)
app.get("/")(read_root)
app.put("/update-config/")(update_config)
app.add_exception_handler(RequestValidationError, validation_exception_handler) 
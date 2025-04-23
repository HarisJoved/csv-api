from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

# Create the security scheme for HTTP Basic authentication
security = HTTPBasic()

# Define a function to check the credentials
def validate_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    # For now, hardcoded credentials
    correct_username = "haris"
    correct_password = "haris"
    
    # Validate the credentials
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    # Return the username if authentication is successful
    return credentials.username

# This dependency function can be used to protect routes
def get_current_user(username: str = Depends(validate_credentials)):
    return {"username": username} 
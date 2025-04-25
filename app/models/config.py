from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class ConfigRequest(BaseModel):
    """Model for the configuration update request."""
    value: str = Field(..., description="Configuration value to update")
    
    class Config:
        json_schema_extra = {
            "example": {
                "value": "new-config-value"
            }
        }

class ConfigResponse(BaseModel):
    """Model for the configuration update response."""
    updated_value: str = Field(..., description="The updated value")
    status: str = Field("success", description="Status of the configuration update")
    message: str = Field("Configuration updated successfully", description="Message regarding the update") 
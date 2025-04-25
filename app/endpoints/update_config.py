from fastapi import Depends, HTTPException, status
from app.auth import get_current_user
from app.models.config import ConfigRequest, ConfigResponse

async def update_config(config: ConfigRequest, current_user: dict = Depends(get_current_user)):
    """
    Update configuration value.
    
    The endpoint requires authentication.
    """
    try:
        # Process the configuration update
        # For now, we just return the updated value
        return ConfigResponse(
            updated_value=config.value,
            status="success",
            message="Configuration updated successfully"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating configuration: {str(e)}"
        ) 
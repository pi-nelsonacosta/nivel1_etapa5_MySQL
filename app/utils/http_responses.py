
responses = {
    401: {
        "description": "Unauthorized - No token provided or token is invalid",
        "content": {
            "application/json": {
                "example": {"detail": "Not authenticated"}
            }
        }
    },
    404: {
        "description": "Not Found - No characters found",
        "content": {
            "application/json": {
                "example": {"detail": "No characters found"}
            }
        }
    },    
}
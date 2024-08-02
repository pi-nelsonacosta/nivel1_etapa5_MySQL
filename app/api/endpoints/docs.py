from fastapi import APIRouter, Request
from fastapi.routing import APIRoute

router = APIRouter()

@router.get("/all-routes", summary="List all routes", description="Get a list of all routes available in the API")
async def get_all_routes(request: Request):
    """
    This endpoint provides a list of all available routes in the API.
    """
    route_list = []
    for route in request.app.routes:
        if isinstance(route, APIRoute):
            route_info = {
                "path": route.path,
                "name": route.name,
                "methods": route.methods,
                "summary": route.summary,
                "description": route.description,
            }
            route_list.append(route_info)
    return route_list

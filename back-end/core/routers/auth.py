from fastapi import APIRouter


router = APIRouter()


@router.get("/auth", include_in_schema=False)
async def auth():
    return "Auth to Hack"


@router.get("/blabla", include_in_schema=False)
async def blabla():
    return "Blabla"
from fastapi import APIRouter


router = APIRouter()


@router.get("/auth")
async def auth():
    return "Auth to Hack"


@router.post("/blabla")
async def blabla():
    return "Blabla"
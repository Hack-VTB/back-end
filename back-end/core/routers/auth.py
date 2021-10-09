from fastapi import APIRouter
from fastapi.responses import JSONResponse
import uuid

from ..db.requests import save_user, create_token, check_user, get_token


router = APIRouter()


@router.post("/register")
async def register(login: str, password: str):
    try:
        user = await save_user({"login": login, "password": password})
        user_id = dict(user)["id"]
        token = uuid.uuid4().hex
        token = await create_token(user_id, token)

        return token
    except:
        return JSONResponse(
            status_code=409, content={"message": "Choose different username"}
        )


@router.get("/obtain")
async def obtain(login: str, password: str):
    user = await check_user(login, password)
    if user is None:
        return JSONResponse(
            status_code=409, content={"message": "Login or password is wrong"}
        )
    user_id = dict(user)["id"]
    token = await get_token(user_id)

    return token

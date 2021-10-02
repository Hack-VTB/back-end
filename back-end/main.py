from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    from core.routers.auth import router as auth_router

    app.include_router(auth_router, tags=["Auth"])

    return app


app = create_app()


@app.get("/")
async def root():
    return "Welcome to the VTB Hack!!!"



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=7000)

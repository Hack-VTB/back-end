from .utils import sql_task


@sql_task
async def create_token(connection, user_id: int, token: str):
    row = await connection.fetchrow(
        "INSERT INTO tokens(user_id, id) VALUES ($1, $2) RETURNING id;", user_id, token
    )

    return row


@sql_task
async def save_user(connection, user_data: dict):
    row = await connection.fetchrow(
        "INSERT INTO users (username, password) VALUES ($1, $2) RETURNING id;",
        user_data["login"],
        user_data["password"],
    )

    return row


@sql_task
async def check_user(connection, username: str, password: str):
    row = await connection.fetchrow(
        "SELECT * FROM Users WHERE username like $1 AND password like $2;",
        username,
        password,
    )

    return row


@sql_task
async def get_token(connection, user_id: int):
    row = await connection.fetchrow(
        "SELECT id FROM Tokens WHERE user_id  = $1;",
        user_id,
    )

    return row

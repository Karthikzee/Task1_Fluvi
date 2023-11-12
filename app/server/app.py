from fastapi import FastAPI, HTTPException, status
from server.constants import PASSWORD_DEFAULT_LEN
from server.exceptions import NegativeValueError
from server.utils import generate_alphanum_password


app = FastAPI()


@app.get("/", tags=["Password Generator"])
async def get_password(max_length: int = PASSWORD_DEFAULT_LEN):  # generate password of given length
    try:
        password = await generate_alphanum_password(max_length)
        return {"password": password[:max_length]}

    except NegativeValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

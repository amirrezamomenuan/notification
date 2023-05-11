from fastapi import Request
from fastapi.responses import JSONResponse

from settings import ALLOWED_SERVICES_SECRET_KEYS


SECRET_HEADER_NAME = "OTP-Secret-Token"


async def otp_secret_middleware(request: Request, call_next):
    secret_token = request.headers.get(SECRET_HEADER_NAME)
    if not secret_token or secret_token not in ALLOWED_SERVICES_SECRET_KEYS:
        return JSONResponse(
            status_code=403,
            content={"message": "otp secret token not provided!"}
        )
    response = await call_next(request)
    return response

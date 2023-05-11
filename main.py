from fastapi import FastAPI

from sms_sender.routers import router as sms_sender_router
from settings import *
from middlewares import otp_secret_middleware

app = FastAPI()


app.include_router(sms_sender_router)
app.middleware("http")(otp_secret_middleware)

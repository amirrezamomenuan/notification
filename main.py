from fastapi import FastAPI

from sms_sender.routers import router as sms_sender_router

app = FastAPI()


app.include_router(sms_sender_router)

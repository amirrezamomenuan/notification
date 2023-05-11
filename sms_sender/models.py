from pydantic import BaseModel


class VerificationCodeRequest(BaseModel):
    phone_number: str
    message: str

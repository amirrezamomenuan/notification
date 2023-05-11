from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests

from .models import VerificationCodeRequest
from settings import KAVENEGAR_SMS_URL

router = APIRouter()


@router.post('/send-verification-code/')
async def send_verification_code(verification_code_request: VerificationCodeRequest):
    data = {
        'receptor': verification_code_request.phone_number,
        'message': verification_code_request.message
    }

    response = requests.post(url=KAVENEGAR_SMS_URL, data=data)
    if response.status_code == 200:
        return JSONResponse(
            status_code=200,
            content={'message': 'verification sms sent successfully'}
        )

    return JSONResponse(
        status_code=400,
        content={'message': 'failed to send sms', 'details': response.text}
    )

from decouple import config, Csv

KAVENEGAR_API_KEY = config('KAVENEGAR_API_KEY')
KAVENEGAR_SMS_URL = config('KAVENEGAR_SMS_URL').format(KAVENEGAR_API_KEY=KAVENEGAR_API_KEY)

ALLOWED_SERVICES_SECRET_KEYS = config('ALLOWED_SERVICES_SECRET_KEYS', cast=Csv())

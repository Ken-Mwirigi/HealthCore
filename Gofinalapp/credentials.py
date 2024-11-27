import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class MpesaC2bCredential:
    consumer_key = 'zM3rGGI5vd8vwywPCknGodTBSNhi2AWgkAHUhG2pqhAMUAOp'
    consumer_secret = 'PwOFR4vlD0MpP3reNkrAUi0PBHy3aaYzkBJhtxzKUhPPq2GdAmOPcaV3gp1czC0G'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')
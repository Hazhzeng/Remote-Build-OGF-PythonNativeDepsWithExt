import json
import numpy
import azure.functions as func
from cryptography.fernet import Fernet


def main(req: func.HttpRequest) -> func.HttpResponse:
    key = Fernet.generate_key()
    fer = Fernet(key)
    token = fer.encrypt(b"A really secret message. Not for prying eyes.")
    decrypted = fer.decrypt(token)

    result = {
        'key': str(key),
        'token': str(token),
        'decrypted': str(decrypted)
    }

    return func.HttpResponse(body=json.dumps(result), mimetype="application/json")

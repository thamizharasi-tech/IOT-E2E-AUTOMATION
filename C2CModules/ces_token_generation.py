import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta
import time

def load_private_key(path):
    with open(path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def load_public_key(path):
    with open(path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )
    return public_key

class JwtService:
    def __init__(self, private_key_path, public_key_path, subject):
        self.private_key = load_private_key(private_key_path)
        self.public_key = load_public_key(public_key_path)
        self.subject = subject

    def generate_token(self):
        headers = {"alg": "RS256", "typ": "JWT"}
        payload = {
            "sub": self.subject,
            "iat": int(time.time())
        }

        #print("Payload: ", payload)
        token = jwt.encode(payload, self.private_key, algorithm="RS256", headers=headers)
        return token

# Example usage
#jwt_service = JwtService("C:\\Car2Cloud_E2ETesting\\C2CtestData\\CES_Demo\\privateKey.pem", "C:\\Car2Cloud_E2ETesting\\C2CtestData\\CES_Demo\\publicKey.pem", "0c88bc5d-c591-4b07-aaf5-b08da08f29ed")
#token = jwt_service.generate_token()
#print("Generated Token:", token)
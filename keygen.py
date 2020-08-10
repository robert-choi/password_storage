import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from p_info import salt

def generate_key(password):
    """
    Generates byte type key from input password
    :return: bytes
    """
    kdf = PBKDF2HMAC(
        algorithm= SHA256(),
        length= 32,
        salt= salt,
        iterations= 100000,
        backend= default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password))

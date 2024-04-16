

import bcrypt


def encrypt_password(password:str):
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt())
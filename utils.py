from settings import global_salt
from hashlib import sha1, md5


def check_password(password: str, pwd_hash: str, salt: str) -> bool:
    return password_hash(password, salt) == pwd_hash


def password_hash(password: str, salt: str) -> str:
    check = global_salt + password + salt
    return sha1(check).hexdigest()
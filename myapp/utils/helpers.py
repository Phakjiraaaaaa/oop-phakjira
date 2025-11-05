import hashlib
import re

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email: str) -> bool:
    """ตรวจสอบว่าอีเมลมีรูปแบบถูกต้องไหม"""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

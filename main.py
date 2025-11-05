from myapp.models.user import User
from myapp.services.auth import login, logout
from myapp.utils.helpers import hash_password, is_valid_email

if __name__ == "__main__":
    user = User("alice", "alice@example.com")

    # ตรวจสอบว่าอีเมลถูกต้องไหม
    if not is_valid_email(user.email):
        print("❌ อีเมลไม่ถูกต้อง❌")
    else:
        password_hash = hash_password("secret")
        if login(user.username, password_hash):
            print("🎉 เข้าสู่ระบบสำเร็จ 🎉")
            logout(user)

from myapp.models.user import User
from myapp.services.auth import login, logout
from myapp.utils.helpers import hash_password

if __name__ == "__main__":
    user = User("alice", "alice@example.com")
    password_hash = hash_password("secret")
    if login(user.username, password_hash):
        print("Login success")
        logout(user)

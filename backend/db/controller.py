from db import session
from db.models import User


def list_users():
    users = session.query(User).all()
    for user in users:
        print(user)

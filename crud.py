from model import User, Project, Task, connect_to_db

def create_user(username, password):
    user = User(
        username = username,
        password=password
    )
    return user

def get_users():
    return User.Query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_username(username):
    return User.query.get(username)

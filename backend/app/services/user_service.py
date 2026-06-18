from app.models.user import User

def create_user(db, username):
    user = User(username=username)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
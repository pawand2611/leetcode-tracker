from app.models.user import User

def create_user(db, username):
    user = User(username=username)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def save_profile(db, profile):

    user = User(
        username=profile["username"],
        real_name=profile["real_name"],
        ranking=profile["ranking"],
        avatar=profile["avatar"],
        easy_solved=profile["easy_solved"],
        medium_solved=profile["medium_solved"],
        hard_solved=profile["hard_solved"],
        total_solved=profile["total_solved"]
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
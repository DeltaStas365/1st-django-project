from django.contrib.auth.models import User
def update_user(user:User, username, email):
    user.username = username
    user.email = email
    user.save()

def change_password(user: User, new_password):
    user.set_password(new_password)
    user.save()
from django.contrib.auth.models import User


def user_auth(account, pwd):
    if '@' in account:
        user = User.objects.filter(email=account)
    else:
        user = User.objects.filter(username=account)
    if not user:
        return None
    user = user.first()
    return user if user.check_password(pwd) else None





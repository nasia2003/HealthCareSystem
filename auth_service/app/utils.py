from .models import UserCus
def simple_auth_usercus(username: str, password: str):
    try:
        user = UserCus.objects.get(username=username)
    except UserCus.DoesNotExist:
        return None

    if user.check_password(password):
        return user
    return None

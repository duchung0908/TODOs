from django.contrib.auth.models import User


def get_user(user_id) -> User:
    try:
        return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Exception("User does not exists!")
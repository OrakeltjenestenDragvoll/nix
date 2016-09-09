from django.contrib.auth.models import User


class FeideBackend(object):
    """
    Authenticate a user with information from Feide
    """

    def authenticate(self, samlUserdata=None):
        try:
            username = samlUserdata['uid'][0]
            try:
                user = User.objects.get(username=username)
                return user
            except User.DoesNotExist:
                return None
        except KeyError:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

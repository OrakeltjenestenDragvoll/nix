from django.contrib.auth.models import User
from django.conf import settings
import uuid


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
                if not any(settings.SAML_EMPLOYEE_STRING in x for x in samlUserdata['eduPersonOrgUnitDN']):
                    return None
                else:
                    user = User.objects.create_user(username, username + '@stud.ntnu.no', uuid.uuid4())
                    user.first_name = samlUserdata['displayName'][0]
                    user.save()
                    return user
        except KeyError:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

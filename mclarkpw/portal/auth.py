from django.contrib.auth.models import User
from .models import AuthToken

class TokenAuthBackend(object):
    def authenticate(self, token=None):
        user = None
        try:
            return AuthToken.current_objects.get(value=token).user
        except:
            return None
        
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
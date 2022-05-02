from ninja.security import HttpBearer
from accounts.models import Token
from django.shortcuts import get_object_or_404


class ApiKey(HttpBearer):
    
    def authenticate(self, request, key):
        if Token.objects.filter(key=key).exists():
            return True


header_key = ApiKey()
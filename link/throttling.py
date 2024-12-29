from rest_framework.throttling import UserRateThrottle
from rest_framework_api_key.models import APIKey

class CreateShortLinkThrottle(UserRateThrottle):
    scope = "create_short_link"

    def get_cache_key(self, request, view):
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        api_key = APIKey.objects.get_from_key(key)
        ident = api_key
        return self.cache_format % {
            "scope": self.scope,
            "ident": ident
        }
    
    def allow_request(self, request, view):
        if request.method == "POST":
            return super().allow_request(request, view)
        return True
        
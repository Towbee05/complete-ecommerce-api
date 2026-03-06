from rest_framework.throttling import SimpleRateThrottle

class AuthenticationBurstThrottle(SimpleRateThrottle):
    scope = "authentication_burst"

    def get_cache_key(self, request, view):
        identity = self.get_ident(request)
        return f"auth_burst_{identity}"

class AuthenticationSustainedThrottle(SimpleRateThrottle):
    scope = "authentication_sustained"

    def get_cache_key(self, request, view):
        identity = self.get_ident(request)

        return f"auth_sustained_{identity}"
    

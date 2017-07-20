from .basicauthutils import validate_request
from .response import HttpResponseUnauthorized
from django.utils.deprecation import MiddlewareMixin


class BasicAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        validated_username = validate_request(request)
        if validated_username is None:
            return HttpResponseUnauthorized()
        else:
            request.META['REMOTE_USER'] = validated_username
            return None

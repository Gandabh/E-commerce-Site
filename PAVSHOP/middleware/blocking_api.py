from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied


class BlackListIPMiddleware(MiddlewareMixin):
    IP_BLACK_LIST = [
        '10.10.80.123'
        # '127.0.0.1'
    ]

    def process_view(self, request, *args, **kwargs):
        ip = request.META['REMOTE_ADDR']
        # print('my ip', ip)
        if ip in self.IP_BLACK_LIST:
            raise PermissionDenied
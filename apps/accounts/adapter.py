from django.conf import settings
from django.shortcuts import resolve_url

from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        if request.user.is_superuser:
            url = 'accounts:dashboard_admin'
        elif request.user.is_staff:
            url = 'accounts:dashboard_staff'
        else:
            url = settings.LOGIN_REDIRECT_URL
            # url = request.META.get('HTTP_REFERER')

        return resolve_url(url)

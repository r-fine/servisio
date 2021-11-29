from django.conf import settings
from django.shortcuts import resolve_url

from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        if request.user.is_superuser:
            url = '/account/admin-dashboard'
        elif request.user.is_staff:
            url = '/account/staff-dashboard'
        else:
            url = settings.LOGIN_REDIRECT_URL

        return resolve_url(url)

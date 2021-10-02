# Middlewares are used for the authentication that whether the user is logged in
# or not, if user is not logged-in we will not allow him to place order
from django.shortcuts import redirect


def auth_middleware(get_response):


    def middleware(request):
        returnUrl = request.META['PATH_INFO']
        if not request.session.get('customer'):
            return redirect(f'login?return_url={returnUrl}')
        response = get_response(request)
        return response

    return middleware
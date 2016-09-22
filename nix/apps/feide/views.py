from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

from onelogin.saml2.auth import OneLogin_Saml2_Auth


def init_saml_auth(req):
    auth = OneLogin_Saml2_Auth(req, custom_base_path=settings.SAML_FOLDER)
    return auth


def prepare_django_request(request):
    # If server is behind proxys or balancers use the HTTP_X_FORWARDED fields
    result = {
        'https': 'on' if request.is_secure() else 'off',
        'http_host': request.META['HTTP_HOST'],
        'script_name': request.META['PATH_INFO'],
        'server_port': request.META['SERVER_PORT'],
        'get_data': request.GET.copy(),
        'post_data': request.POST.copy()
    }
    return result


@csrf_exempt
def login(request):
    req = prepare_django_request(request)
    auth = init_saml_auth(req)

    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    if request.method == 'GET': 
        return HttpResponseRedirect(auth.login())

    if request.method == 'POST':
        auth.process_response()
        errors = auth.get_errors()

        if not errors:
            request.session['samlUserdata'] = auth.get_attributes()
            request.session['samlNameId'] = auth.get_nameid()
            request.session['samlSessionIndex'] = auth.get_session_index()
            user = authenticate(samlUserdata=auth.get_attributes())

            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect("/")

            return HttpResponseForbidden(str("Access denied!"), content_type="text/plain")

        if settings.DEBUG:
            str_errors = ",".join(errors)
            return HttpResponseServerError(str_errors + ': ' + auth.get_last_error_reason(), content_type="text/plain")
        else:
            return HttpResponseServerError("An error occured. Could not login!", content_type="text/plain")


def logout(request):

    if request.user.is_authenticated():
        req = prepare_django_request(request)
        auth = init_saml_auth(req)

        if request.GET.get('SAMLResponse') is not None:
            dscb = lambda: request.session.flush()
            url = auth.process_slo(delete_session_cb=dscb)
            errors = auth.get_errors()
            if not errors:
                if url is not None:
                    return HttpResponseRedirect(url)
                else:
                    return HttpResponseRedirect(auth.login())

        else:
            name_id = None
            session_index = None
            if 'samlNameId' in request.session:
                name_id = request.session['samlNameId']
            if 'samlSessionIndex' in request.session:
                session_index = request.session['samlSessionIndex']

            return HttpResponseRedirect(auth.logout(name_id=name_id, session_index=session_index))

    return HttpResponse("Not logged in.", content_type="text/plain")

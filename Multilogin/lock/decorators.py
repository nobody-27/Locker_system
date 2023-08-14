
import functools
from django.shortcuts import redirect,HttpResponse
from django.http import HttpResponseBadRequest,HttpResponseForbidden
from django.contrib.sessions.backends.db import SessionStore


def check_pin_for(function):    
    def wrap(request, *args, **kwargs):
        session_id = request.session.get('session_id_data',None)
        print(session_id,"this is session id")
        if session_id is not None:
            return function(request, *args, **kwargs)
        else:
            return redirect('pin')
        # return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
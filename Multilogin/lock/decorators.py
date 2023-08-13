
import functools
from django.shortcuts import redirect,HttpResponse
from django.http import HttpResponseBadRequest,HttpResponseForbidden
from django.contrib.sessions.backends.db import SessionStore


def check_pin_for(function):    
    def wrap(request, *args, **kwargs):
        # if request.user.is_superuser:
        #     print(request.user,"this is superuser")
        #     return function(request, *args, **kwargs)
        # else:
        #     print("user is not superuser")
        #     return redirect('pin')


        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
from typing import Any
from django.conf import settings
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect
import re

class SimpleMiddlewareStructure:

    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        
        # Code that is executed in each request before the view is called
        response = self.get_response(request)

        # Code that is executed in each request after the view is called
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called
        pass

    def process_exception(self, request, exception):
        print(exception)
        # This code is executed if an exception is raised
        pass

    def process_template_response(self, request, response):
        # This code is executed if the response contains a render() method
        return response
    



class EnforceLoginMiddleware(object):

    def __init__(self,get_response) -> None:
        self.get_response = get_response

        self.login_url = getattr(settings,'LOGIN_URL','/accounts/login/')
        print(self.login_url,"")

        if hasattr(settings,'PUBLIC_URLS'):
            public_urls = [re.compile(url) for url in settings.PUBLIC_URLS]

            public_urls_2 = [url for url in settings.PUBLIC_URLS]

        print(public_urls_2,"url 3")


        public_urls.append(re.compile("^%s$" % ( self.login_url[1:] )))
        self.public_urls = tuple(public_urls)
        print(self.public_urls,"urls..")


    def __call__(self, request):

        if request.user.is_anonymous:
            for url in self.public_urls:
                if url.match(request.path[1:]):
                    break
            else:
                print(request.path,"test")
                # redirect_url_1 = "/%s?next=%s" % (self.login_url,request.path)
                # print(redirect_url_1,"redirect_url_1")
                redirect_url = f'/{self.login_url}/?next={request.path}'
                # return redirect(self.login_url)
                return HttpResponseRedirect(redirect_url)

        response = self.get_response(request)
        return response

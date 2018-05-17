from django.http.response import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json


class AuthView(View):
    form_class = None

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        # form = self.form_class(body)
        return HttpResponse()

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AuthView, self).dispatch(*args, **kwargs)

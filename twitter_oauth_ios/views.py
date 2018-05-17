from django.http.response import HttpResponse
from django.views import View


class AuthView(View):
    form_class = None

    def post(self, request, *args, **kwargs):
        # form = self.form_class(request.POST)
        return HttpResponse()

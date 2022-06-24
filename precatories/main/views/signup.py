from django.http import HttpResponse
from django.template import loader


def signup_view(request):
    template = loader.get_template('login/signup.html')
    return HttpResponse(template.render({}, request))

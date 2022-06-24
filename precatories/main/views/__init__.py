from django.http import HttpResponse
from django.template import loader

from .login import login_view


def index(request):
    return login_view(request)

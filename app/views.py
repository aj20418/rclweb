from django.http import HttpResponse


def load_temp(name):
    with open('./templates/{}'.format(name)) as f:
        return f.read()


def index(request):
    return HttpResponse(load_temp('index.html'))


def signup(request):
    return HttpResponse(load_temp('signup.html'))


def success(request):
    return HttpResponse(load_temp('signup.php'))

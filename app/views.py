from django.http import HttpResponse


def index(request):
    with open('./index.html') as f:
        response = f.read()
    return HttpResponse(response)

from django.http import HttpResponse

def index(request):
    print(request.method)
    return HttpResponse("Hello world!")
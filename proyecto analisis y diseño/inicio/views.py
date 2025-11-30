from django.http import HttpResponse

# Create your views here.
def hol(request):
    return HttpResponse("<h2>Eso Tilin<h2>")
def hol2(resquest):
    return HttpResponse('About')
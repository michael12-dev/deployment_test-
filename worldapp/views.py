from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'index.html')

def worldview(request):
    return render (request, 'rubbish.html')
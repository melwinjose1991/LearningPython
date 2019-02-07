from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Here index is a view
def index(request):
    my_dict = {'insert_me' : 'From first_app\\views.py'}
    return render(request, "first_app/index.html", context=my_dict)

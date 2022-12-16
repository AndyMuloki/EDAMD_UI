from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

# request -> response
# request handler
# action

rooms = [
    {'id':1, 'name':'Lets Learn python!'},
    {'id':2, 'name':'Lets go!'},
    {'id':3, 'name':'Lets Design!'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'cnn/home.html', context)


def room(request):
    return render(request, 'cnn/room.html')
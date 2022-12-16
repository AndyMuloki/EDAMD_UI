from django.shortcuts import render
from .models import Room
# from django.http import HttpResponse

# Create your views here.

# request -> response
# request handler
# action

rooms = [
    {'id':1, 'name':'Get Diagnosed Now!'},
    {'id':2, 'name':'Schedule an Appointment with us'},
    
]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'cnn/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'cnn/room.html', context)
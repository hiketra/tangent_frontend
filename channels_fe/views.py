from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
def chatroom(request):
    return render(request, 'chatroom.html')

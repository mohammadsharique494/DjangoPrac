from django.shortcuts import render
rooms = [
    {'id':1 , 'name':'let learns python'},
    {'id':2 , 'name':'Springboot is fun'},
    {'id':3 , 'name':'lets build api with Django'},
    {'id':4 , 'name':'Deployment'},
    
]
# Create your views here.
def home(request):
    context ={'rooms':rooms}
    return render(request , 'base/home.html', context)
def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room=i
    context ={'room':room}
    return render(request,'base/room.html',context)
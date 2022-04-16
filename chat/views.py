from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.
def home(request):
    return render(request, 'home.html')


def room(request, room):
    context = {
        'room': room,
        'room_details': Room.objects.filter(name=room).first(),
        'username': request.GET.get('username')
    }
    return render(request, 'room.html', context)


def check_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        username = request.POST.get('username')
        room, created = Room.objects.get_or_create(name=room_name)
        return redirect(f'/{room.name}/?username={username}')


def send_message(request):
    if request.method == 'POST':
        message_content = request.POST.get('message')
        username = request.POST.get('username')
        room = request.POST.get('room_id')
        message = Message.objects.create(content=message_content, user=username, room=Room.objects.get(id=room))
        return HttpResponse('message sent')
            

def get_messages(request, room):
    messages = Message.objects.filter(room__name=room)
    return JsonResponse({'messages': list(messages.values())})
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
def rooms_list(request):
    rooms = Room.objects.all()
    print(rooms)
    return render(request,"bookings/rooms_list.html, stations")
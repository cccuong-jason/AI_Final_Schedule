from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from .forms import *
from .models import *
post = [
    {
        'name': 'Cuong',
        'Course': 'CS001',
        'Room': 'C201',
        'Shift': '1'
    },
    {
        'name': 'Loc',
        'Course': 'CS002',
        'Room': 'C202',
        'Shift': '2'
    },
    {
        'name': 'Mai',
        'Course': 'CS003',
        'Room': 'C203',
        'Shift': '3'
    }
    
]

def home(request):
    context = {
        'schedule': post
    }
    return render(request, 'home.html', context)

def add_instructor(request):
    dup = ''
    form = InstructorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and Instructors.objects.filter(Ins_id=request.POST['Ins_id']).exists() == False:
            form.save()
            dup = False
            messages.success(request, "Successfully Added!")
            context = {
                'form': form,
                'dup': False
            }
            return render(request, 'ins.html', context)
        dup = True
    if dup == True:
        messages.warning(request, "Duplicated Ins_id!")
        context = {
            'form': form,
            'dup': True
        }
    elif dup == False:
        messages.success(request, "Successfully Added!")
        context = {
            'form': form,
            'dup': False
        }
    else:
        messages.info(request, "You can add or edit instructors here!")
        context = {
            'form': form,
            'dup': ''
        }
    return render(request, 'ins.html', context)

def inst_list_view(request):
    context = {
        'instructors': Instructors.objects.all()
    }
    return render(request, 'instlist.html', context)

def delete_instructor(request, pk):
    inst = Instructors.objects.filter(pk=pk)
    if request.method == 'POST':
        inst.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('editinstructors')

def add_room(request):
    dup = ''
    form = RoomForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and (Room.objects.filter(r_number=request.POST['r_number']).exists() == False and Room.objects.filter(r_name=request.POST['r_name']).exists() == False) :
            form.save()
            rdup = False
            messages.success(request, "Successfully Room Added!")
            context = {
                'form': form,
                'dup': False,
                'room': Room.objects.all()
            }
            return render(request, 'room.html', context)
        dup = True
    if dup == True:
        messages.warning(request, "Duplicated Id or Name!")
        context = {
            'form': form,
            'dup': True,
            'room': Room.objects.all()
        }
    elif dup == False:
        messages.success(request, "Successfully Room Added!")
        context = {
            'form': form,
            'dup': False,
            'room': Room.objects.all()
        }
    else:
        messages.info(request, "You can add or delete Room here!")
        context = {
            'form': form,
            'dup': '',
            'room': Room.objects.all()
        }
    print(Room.objects.all())
    return render(request, 'room.html', context)

# Create your views here.

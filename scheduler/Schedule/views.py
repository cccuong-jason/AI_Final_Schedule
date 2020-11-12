from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages 
from .forms import *
from .models import *
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
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
        messages.error(request, "Duplicated Ins_id!")
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
        messages.error(request, "Duplicated Id or Name!")
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
    return render(request, 'room.html', context)

def delete_room(request, pk):
    inst = Room.objects.filter(pk=pk)
    print('Inst: ',inst)
    if request.method == 'POST':
        inst.delete()
        messages.success(request, "Successfully deleted!")
        return redirect('addrooms')

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid() and (Room.objects.filter(r_number=request.POST['r_number']).exists() == False or Room.objects.filter(r_name=request.POST['r_name']).exists() == False):
            form.save()
            messages.success(request, "Successfully Room Edited!")
            return redirect('addrooms')
    messages.error(request, "Duplicated Id or Name!")
    context = {
        'form': form,
        'room': Room.objects.all()
    }
    return render(request, 'room.html', context)




# Create your views here.


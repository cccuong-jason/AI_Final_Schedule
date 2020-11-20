from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages 
from .forms import *
from .models import *
from django.urls import reverse_lazy
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
'''
Home return
'''
def home(request):
    context = {
        'schedule': post
    }
    return render(request, 'home.html', context)

'''
Add instructor
'''
def add_instructor(request):
    dup = ''
    form = InstructorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and Instructors.objects.filter(Ins_id=request.POST['Ins_id']).exists() == False:
            form.save()
            dup = False
            messages.success(request, "Successfully ["+request.POST['Ins_id']+" - "+request.POST['Ins_name']+"] Added!")
            context = {
                'form': form,
                'dup': False
            }
            return render(request, 'ins.html', context)
        dup = True
    if dup == True:
        messages.error(request, "Duplicated Instructor's Id or Name!")
        context = {
            'form': form,
            'dup': True
        }
    elif dup == False:
        messages.success(request, "Successfully ["+request.POST['Ins_id']+" - "+request.POST['Ins_name']+"] Added!")
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

'''
View list Instructors
'''
def inst_list_view(request):
    context = {
        'instructors': Instructors.objects.all()
    }
    return render(request, 'instlist.html', context)

'''
Delete list Instructors
'''
def delete_instructor(request, pk):
    inst = Instructors.objects.filter(pk=pk)
    Ins_id = ins.values_list('Ins_id', flat=True).get(pk=pk)
    Ins_name = ins.values_list('Ins_name', flat=True).get(pk=pk)
    if request.method == 'POST':
        inst.delete()
        messages.success(request, "Successfully ["+Ins_id+" - "+Ins_name+"] Deleted!")
        return redirect('editinstructors')

'''
Add rooms
'''

def add_room(request):
    dup = ''
    form = RoomForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and (Room.objects.filter(r_number=request.POST['r_number']).exists() == False and Room.objects.filter(r_name=request.POST['r_name']).exists() == False) :
            form.save()
            dup = False
            messages.success(request, "Successfully ["+request.POST['r_number']+" - "+request.POST['r_name']+"] Added!")
            context = {
                'form': form,
                'dup': False,
                'room': Room.objects.all()
            }
            return render(request, 'room.html', context)
        dup = True
    if dup == True:
        messages.error(request, "Duplicated Room's Id or Name!")
        context = {
            'form': form,
            'dup': True,
            'room': Room.objects.all()
        }
    elif dup == False:
        messages.success(request, "Successfully ["+request.POST['Ins_id']+" - "+request.POST['Ins_name']+"] Added!")
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

'''
Delete rooms
'''

def delete_room(request, pk):
    room = Room.objects.filter(pk=pk)
    r_number = room.values_list('r_number', flat=True).get(pk=pk)
    r_name = room.values_list('r_name', flat=True).get(pk=pk)
    if request.method == 'POST':
        room.delete()
        messages.success(request, "Successfully ["+r_number+" - "+r_name+"] Deleted!")
        return redirect('addrooms')

'''
Update rooms
'''

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid() and (Room.objects.filter(r_number=request.POST['r_number']).exists() == False or Room.objects.filter(r_name=request.POST['r_name']).exists() == False):
            form.save()
            messages.success(request, "Successfully ["+request.POST['r_number']+" - "+request.POST['r_name']+"] Edited!")
            return redirect('addrooms')
    messages.error(request, "Duplicated Room's Id or Name!")
    context = {
        'form': form,
        'room': Room.objects.all()
    }
    return render(request, 'room.html', context)

'''
Add subjects
'''

def add_subject(request):
    dup = ''
    form = SubjectForm(request.POST or None)
    objectlist = Instructors.objects.all()
    n = Subject.sj_ins.through.objects.all()
    temp = []
    current = []
    for x in Subject.objects.all():
                for i in n:
                    for z in objectlist:
                        if x.id == i.subject_id and i.instructors_id == z.id:
                            temp.append((i.subject_id,x.sj_id,x.sj_name,z.Ins_name,z.Ins_id,z.id))
    for x in objectlist:
        current.append([x.Ins_id,x.Ins_name,x.id])
    subs = []
    for z in range(len(current)):
        for y in n:
            if y.instructors_id == current[z][2]:
                subs.append(y.subject_id)
        current[z].append(subs)        
        subs = []
    if request.method == 'POST':
        temp1 = []
        subs1 = []
        current1 = []
        if form.is_valid() and (Subject.objects.filter(sj_id=request.POST['sj_id']).exists() == False and Subject.objects.filter(sj_name=request.POST['sj_name']).exists() == False) :
            form.save()
            dup = False
            n.update()
            messages.success(request, "Successfully ["+request.POST['sj_id']+" - "+request.POST['sj_name']+"] Added!")
            for x in Subject.objects.all():
                for i in n:
                    for z in objectlist:
                        if x.id == i.subject_id and i.instructors_id == z.id:
                            temp1.append((i.subject_id,x.sj_id,x.sj_name,z.Ins_name))

            objectlist.update()
            n.update()
            for x in objectlist:
                current1.append([x.Ins_id,x.Ins_name,x.id])
            for z in range(len(current)):
                for y in n:
                    if y.instructors_id == current[z][2]:
                        subs1.append(y.subject_id)
                current1[z].append(subs1)        
                subs1 = []
            context = {
                'form': form,
                'dup': False,
                'subject': Subject.objects.all(),
                'list_ins': current1,
                'table': n,
                'insSub': temp1
            }
            return render(request, 'subject.html', context)
        dup = True
    if dup == True:
        messages.error(request, "Duplicated Subject's Id or Name!")
        context = {
            'form': form,
            'dup': True,
            'subject': Subject.objects.all(),
            'list_ins': current,
            'table': n,
            'insSub': temp
        }
    elif dup == False:
        messages.success(request, "Successfully ["+request.POST['sj_id']+" - "+request.POST['sj_name']+"] Added!")
        context = {
            'form': form,
            'dup': False,
            'subject': Subject.objects.all(),
            'list_ins': current,
            'table': n,
            'insSub': temp
        }
    else:
        messages.info(request, "You can add or delete Subject here!")
        context = {
            'form': form,
            'dup': '',
            'subject': Subject.objects.all(),
            'list_ins': current,
            'table': n,
            'insSub': temp
        }
    return render(request, 'subject.html', context)

'''
Delete subjects
'''

def delete_subject(request, pk):
    subject = Subject.objects.filter(pk=pk)
    sj_id = subject.values_list('sj_id', flat=True).get(pk=pk)
    sj_name = subject.values_list('sj_name', flat=True).get(pk=pk)
    if request.method == 'POST':
        subject.delete()
        messages.success(request, "Successfully ["+sj_id+" - "+sj_name+"] Deleted!")
        return redirect('addsubjects')

'''
Update subjects
'''

def update_subject(request, pk):
    subj = Subject.objects.get(id=pk)
    form = SubjectForm(request.POST)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subj)
        if form.is_valid() and (Subject.objects.filter(sj_id=request.POST['sj_id']).exists() == False or Subject.objects.filter(sj_name=request.POST['sj_name']).exists() == False):
            #  and (Subject.objects.filter(sj_id=request.POST['sj_id']).exists() == False or Subject.objects.filter(sj_name=request.POST['sj_name']).exists() == False):
            form.save()
            messages.success(request, "Successfully ["+request.POST['sj_id']+" - "+request.POST['sj_name']+"] Edited!")
            return redirect('addsubjects')
    messages.error(request, "Duplicated Subject's Id or Name!")
    # return render(request, 'subject.html', context)
    return redirect('addsubjects')

'''
Add shifts
'''

def add_shift(request):
    dup = ''
    form = ShiftForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and (Shift.objects.filter(sid=request.POST['sid']).exists() == False) :
            form.save()
            dup = False
            messages.success(request, "Successfully ["+request.POST['time']+" - "+request.POST['day']+"] Added!")
            context = {
                'form': form,
                'dup': False,
                'shift': Shift.objects.all()
            }
            return render(request, 'shift.html', context)
        dup = True
    if dup == True:
        messages.error(request, "Duplicated Shift's Id!")
        context = {
            'form': form,
            'dup': True,
            'shift': Shift.objects.all()
        }
    elif dup == False:
        messages.success(request, "Successfully ["+request.POST['time']+" - "+request.POST['day']+"] Added!")
        context = {
            'form': form,
            'dup': False,
            'shift': Shift.objects.all()
        }
    else:
        messages.info(request, "You can add or delete Shift here!")
        context = {
            'form': form,
            'dup': '',
            'shift': Shift.objects.all()
        }
    return render(request, 'shift.html', context)

'''
Delete shifts
'''

def delete_shift(request, pk):
    shift = Shift.objects.filter(pk=pk)
    time = shift.values_list('time', flat=True).get(pk=pk)
    day = shift.values_list('day', flat=True).get(pk=pk)
    if request.method == 'POST':
        shift.delete()
        messages.success(request, "Successfully ["+time+" - "+day+"] Deleted!")
        return redirect('addshifts')

'''
Update shifts
'''

def update_shift(request, pk):
    shift = Shift.objects.get(id=pk)
    form = ShiftForm(instance=shift)
    if request.method == 'POST':
        form = ShiftForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully ["+request.POST['time']+" - "+request.POST['day']+"] Edited!")
            return redirect('addshifts')
        messages.error(request, "Duplicated Shift's Id!")
    context = {
        'form': form,
        'shift': Shift.objects.all()
    }
    
    return render(request, 'shift.html', context)

'''
Add Departments
'''

def add_department(request):
    dup = ''
    form = DepartmentForm(request.POST or None)
    objectlist = Subject.objects.all()
    n = Department.subjects.through.objects.all()
    temp = []
    current = []
    for x in Subject.objects.all():
                for i in n:
                    for z in Department.objects.all():
                        if x.id == i.subject_id and i.department_id == z.id:
                            temp.append((z.id,z.dept_name,x.sj_name))
    for x in objectlist:
        current.append([x.id,x.sj_name,x.sj_id])
    subs = []
    for z in range(len(current)):
        for y in n:
            if y.subject_id == current[z][0]:
                subs.append(y.department_id)
        current[z].append(subs)        
        subs = []
    if request.method == 'POST':
        temp1 = []
        subs1 = []
        current1 = []
        if form.is_valid() and (Department.objects.filter(dept_name=request.POST['dept_name']).exists() == False) :
            form.save()
            dup = False
            n.update()
            messages.success(request, "Successfully ["+request.POST['dept_name']+"] Added!")
            for x in Subject.objects.all():
                for i in n:
                    for z in Department.objects.all():
                        if x.id == i.subject_id and i.department_id == z.id:
                            temp1.append((z.id,z.dept_name,x.sj_name))
            n.update()
            objectlist.update()
            for x in objectlist:
                current1.append([x.id,x.sj_name,x.sj_id])
            for z in range(len(current)):
                for y in n:
                    if y.subject_id == current[z][0]:
                        subs1.append(y.department_id)
                current1[z].append(subs1)        
                subs1 = []
            
            context = {
                'form': form,
                'dup': False,
                'department': Department.objects.all(),
                'list_sj': current1,
                # 'table': n,
                'deptSub': temp1
            }
            return render(request, 'department.html', context)
        dup = True
    if dup == True:
        messages.error(request, "Duplicated Department's Name!")
        context = {
            'form': form,
            'dup': True,
            'department': Department.objects.all(),
            'list_sj': current,
            # 'table': n,
            'deptSub': temp
        }
    elif dup == False:
        messages.success(request, "Successfully ["+request.POST['dept_name']+"] Added!")
        context = {
            'form': form,
            'dup': False,
            'department': Department.objects.all(),
            'list_sj': current,
            # 'table': n,
            'deptSub': temp
        }
    else:
        messages.info(request, "You can add or delete Subject here!")
        context = {
            'form': form,
            'dup': '',
            'department': Department.objects.all(),
            'list_sj': current,
            # 'table': n,
            'deptSub': temp
        }
    return render(request, 'department.html', context)

'''
Delete Departments
'''

def delete_department(request, pk):
    department = Department.objects.filter(pk=pk)
    dept_name = department.values_list('dept_name', flat=True).get(pk=pk)
    if request.method == 'POST':
        department.delete()
        messages.success(request, "Successfully ["+dept_name+"] Deleted!")
        return redirect('adddepartments')

'''
Update Departments
'''

def update_department(request, pk):
    dept = Department.objects.get(id=pk)
    form = DepartmentForm(request.POST)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid() and (Subject.objects.filter(dept_name=request.POST['dept_name']).exists() == False):
            #  and (Subject.objects.filter(sj_id=request.POST['sj_id']).exists() == False or Subject.objects.filter(sj_name=request.POST['sj_name']).exists() == False):
            form.save()
            messages.success(request, "Successfully ["+request.POST['dept_name']+"] Edited!")
            return redirect('adddepartments')
    messages.error(request, "Duplicated Department's Name!")
    # return render(request, 'subject.html', context)
    return redirect('adddepartments')

'''
Add section
'''

def add_section(request):
    dup = ''
    form = SectionForm(request.POST or None)
    department = Department.objects.all()
    if request.method == 'POST':
        if form.is_valid() and (Section.objects.filter(section_id=request.POST['section_id']).exists() == False) :
            form.save()
            dup = False
            messages.success(request, "Successfully ["+request.POST['section_id']+" - "+request.POST['department']+"] Added!")
            context = {
                'form': form,
                'dup': False,
                'section': Section.objects.all(),
                'list_department': department
            }
            return render(request, 'section.html', context)
        dup = True
    if dup == True:
        messages.error(request, "Duplicated Section's Id or Department!")
        context = {
            'form': form,
            'dup': True,
            'section': Section.objects.all(),
            'list_department': department
        }
    elif dup == False:
        messages.success(request, "Successfully ["+request.POST['section_id']+" - "+request.POST['department']+"] Added!")
        context = {
            'form': form,
            'dup': False,
            'section': Section.objects.all(),
            'list_department': department
        }
    else:
        messages.info(request, "You can add or delete Section here!")
        context = {
            'form': form,
            'dup': '',
            'section': Section.objects.all(),
            'list_department': department
        }
    return render(request, 'section.html', context)

'''
Delete shifts
'''

def delete_section(request, pk):
    print(pk)
    sec = Section.objects.filter(pk=pk)
    section_id = sec.values_list('section_id', flat=True).get(pk=pk)
    department = sec.values_list('department', flat=True).get(pk=pk)
    if request.method == 'POST':
        sec.delete()
        messages.success(request, "Successfully ["+section_id+" - "+department+"] Deleted!")
        return redirect('addsections')

'''
Update shifts
'''

def update_section(request, pk):
    section = Section.objects.get(pk=pk)
    form = SectionForm(instance=section)
    department = Department.objects.all()
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        print(form)
        if form.is_valid() and Section.objects.filter(department=request.POST['department']).exists() == False:
            form.save()
            messages.success(request, "Successfully ["+request.POST['section_id']+" - "+request.POST['department']+"] Edited!")
            return redirect('addsections')
        messages.error(request, "Duplicated Section's Id or Department!")
    context = {
        'form': form,
        'section': Section.objects.all(),
        'list_department': department
    }
    
    return render(request, 'section.html', context)
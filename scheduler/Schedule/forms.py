from django import forms
from django.forms import ModelForm
from. models import *

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'r_number',
            'r_name'
        ]


class InstructorForm(ModelForm):
    class Meta:
        model = Instructors
        fields = [
            'Ins_id',
            'Ins_name'
        ]
        
class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['sj_id', 'sj_name', 'sj_ins','sj_classes']
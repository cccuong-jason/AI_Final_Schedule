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
    def clean(self):
        cleaned_data = self.cleaned_data
        r_number = cleaned_data.get('r_number')
        qs = Room.objects.filter(r_number__iexact=r_number)
        print('qs: ',qs)
        print(self.instance.pk)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
            print('qs after: ',qs)
        if qs.exists():
            raise forms.ValidationError("This shift already exists.")
        return cleaned_data

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

    def clean(self):
        cleaned_data = self.cleaned_data
        sj_id = cleaned_data.get('sj_id')
        sj_name = cleaned_data.get('sj_name')
        qs = Subject.objects.filter(sj_id__iexact=sj_id)
        qs1 = Subject.objects.filter(sj_name__iexact=sj_name)
        print('qs: ',qs)
        print(self.instance.pk)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
            qs1 = qs1.exclude(pk=self.instance.pk)
            print('qs after: ',qs)
        if qs.exists() and qs1.exists():
            raise forms.ValidationError("This shift already exists.")
        return cleaned_data
        

class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields = ['sid','time','day']
        
    # def clean(self):
    #     qs = ShiftForm.Meta.model.objects.filter(sid__iexact=ShiftForm.Meta.fields[0])
    #     if self.instance:  # not sure if it should be self.instance.pk
    #         qs = qs.exclude(pk=self.instance.pk)
    #     if qs.exists():
    #         raise forms.ValidationError("This shift already exists.") 
    def clean(self):
        cleaned_data = self.cleaned_data
        sid = cleaned_data.get('sid')
        time = cleaned_data.get('time')
        day = cleaned_data.get('day')
        qs = Shift.objects.filter(sid__iexact=sid)
        qs1 = Shift.objects.filter(time__iexact=time)
        qs2 = Shift.objects.filter(day__iexact=day)
        if self.instance:  # not sure if it should be self.instance.pk
            qs = qs.exclude(pk=self.instance.pk)
            qs1 = qs1.exclude(pk=self.instance.pk)
            qs1 = qs1.exclude(pk=self.instance.pk)
        if qs.exists() and qs1.exists() and qs2.exists():
            raise forms.ValidationError("This shift already exists.")

        """ This is the form's clean method, not a particular field's clean method """
        time = cleaned_data.get("time")
        day = cleaned_data.get("day")
        if Shift.objects.filter(time=time, day=day).count() > 0:
           del cleaned_data["time"]
           del cleaned_data["day"]
           raise forms.ValidationError("Time and Day combination already exists.")
        return cleaned_data

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'subjects']

    def clean(self):
        cleaned_data = self.cleaned_data
        dept_name = cleaned_data.get('dept_name')
        qs = Department.objects.filter(dept_name__iexact=dept_name)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This shift already exists.")
        return cleaned_data

class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_id', 'department', 'classes_in_week']
    def clean(self):
        cleaned_data = self.cleaned_data
        section_id = cleaned_data.get('section_id')
        qs = Section.objects.filter(section_id__iexact=section_id)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
            print(qs)
        if qs.exists():
            raise forms.ValidationError("This section already exists.")
        print('Cleaned data: ',cleaned_data)
        return cleaned_data

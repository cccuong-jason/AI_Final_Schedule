from django.db import models

# Create your models here.
'''
Instructors Model
'''
class Instructors(models.Model):
    Ins_id = models.CharField(max_length=4)
    Ins_name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Ins_id} {self.Ins_name}'

'''
Room Model
'''
class Room(models.Model):
    r_number = models.CharField(max_length=5)
    r_name = models.CharField(max_length=5)
    seating_capacity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.r_number} {self.r_name} {self.seating_capacity}'

'''
Subject Model
'''
class Subject(models.Model):
    sj_id = models.CharField(max_length=6)
    sj_name = models.CharField(max_length=50)
    sj_ins = models.ManyToManyField(Instructors)
    max_numb_students = models.CharField(max_length=65)

    @property
    def get_ins(self):
        return self.sj_ins

    def __str__(self):
        return f'{self.sj_id} {self.sj_name} {self.sj_ins}'


class Shift(models.Model):
    sid = models.CharField(max_length=5)
    time = models.CharField(max_length=50)
    day = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.sid} {self.day} {self.time}'
    
    class Meta:
        unique_together = ('time','day')

class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject)

    @property
    def get_courses(self):
        return self.subjects

    def __str__(self):
        return self.dept_name

class Section(models.Model):
    section_id = models.CharField(max_length=25, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    classes_in_week = models.IntegerField(default=0)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE, blank=True, null=True)
    instructor = models.ForeignKey(Instructors, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ('section_id','department')
    
    def set_room(self, room):
        section = Section.objects.get(pk = self.section_id)
        section.room = room
        section.save()

    def set_shift(self, shift):
        section = Section.objects.get(pk = self.section_id)
        section.shift = shift
        section.save()

    def set_instructor(self, instructor):
        section = Section.objects.get(pk=self.section_id)
        section.instructor = instructor
        section.save()

    def __str__(self):
        return f'{self.section_id}{self.department}{self.classes_in_week}'
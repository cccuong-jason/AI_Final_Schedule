from django.db import models

# Create your models here.


shifts = (
    ('Shift 1', '6:50 - 9:15'),
    ('Shift 2', '9:25 - 11:50'),
    ('Shift 3', '12:30 - 14:55'),
    ('Shift 4', '15:05 - 17:30'),
    ('Shift 5', '17:45 - 21:00'),

)
DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday')
)
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
    def __str__(self):
        return f'{self.r_number} {self.r_name}'

'''
Subject Model
'''
class Subject(models.Model):
    sj_id = models.CharField(max_length=6)
    sj_name = models.CharField(max_length=50)
    sj_ins = models.ManyToManyField(Instructors)
    sj_classes = models.IntegerField()

    @property
    def get_ins(self):
        return self.sj_ins

    def __str__(self):
        return f'{self.sj_id} {self.sj_name} {self.sj_ins}'

class Shift(models.Model):
    sid = models.CharField(max_length=4, primary_key=True)
    time = models.CharField(max_length=50, choices=shifts, default='6:50 - 9:15')
    day = models.CharField(max_length=15, choices=DAYS_OF_WEEK)

    def __str__(self):
        return f'{self.sid} {self.day} {self.time}'

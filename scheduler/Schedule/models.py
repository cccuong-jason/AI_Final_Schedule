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

    def __str__(self):
        return f'{self.sj_id} {self.sj_name}'



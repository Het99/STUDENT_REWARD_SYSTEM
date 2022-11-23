from operator import truediv
from django.db import models

# Create your models here.

class student(models.Model):
    student_ID = models.IntegerField(primary_key=truediv)
    student_name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)

    def __str__(self):
        return str(self.student_ID)


class admin(models.Model):
    admin_ID = models.IntegerField(primary_key=truediv)
    admin_name = models.CharField(max_length=60)

    def __str__(self):
        return str(self.admin_ID)

class instructor(models.Model):
    instructor_ID = models.IntegerField(primary_key=truediv)
    instructor_name = models.CharField(max_length=60)
    instructor_address = models.CharField(max_length=60)
    admin_ID = models.ForeignKey(admin,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.instructor_ID)

class course(models.Model):
    course_ID = models.IntegerField(primary_key=truediv)
    course_name = models.CharField(max_length=60)
    instructor_ID = models.ForeignKey(instructor,on_delete=models.CASCADE)


class reward(models.Model):
    rank = models.IntegerField(primary_key=truediv)
    reward_name = models.CharField(max_length=60)


class combined_scale(models.Model):
    instructor_ID = models.ForeignKey(instructor,on_delete=models.CASCADE,primary_key=truediv)
    academic_scale = models.FloatField()
    non_academic_scale = models.FloatField()


class performance(models.Model):
    student_ID = models.ForeignKey(student,on_delete=models.CASCADE,primary_key=truediv)
    performance = models.FloatField()
    




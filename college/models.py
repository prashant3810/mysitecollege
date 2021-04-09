from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_mail = models.TextField(unique=True)
    ssc_marks = models.IntegerField()
    pu_marks = models.IntegerField()
    phone_num = models.IntegerField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        self.student_name


class StudentReg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    student_dep = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/',blank=True, null=True)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=200)
    staff_dep = models.TextField()
    staff_mail = models.TextField()
    staff_phone_num = models.IntegerField()
    staff_qualifications = models.TextField()
    staff_experience = models.IntegerField()
    def __str__(self):
        self.staff_name


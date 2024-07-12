from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.DateTimeField(auto_now_add=True)


class Teachers(models.Model):
    full_name = models.CharField(max_length=200)
    status = models.CharField(max_length=150)
    experience = models.CharField(max_length=200)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

class Students(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.IntegerField(max_length=13)
    parents_phone_number = models.IntegerField(max_length=13)
    telegram_link = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
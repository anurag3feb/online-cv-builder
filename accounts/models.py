from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
SeniorSecondaryChoices=(('Art','Arts'),
                        ('Commerce','Commerce'),
                        ('Science','Science'))


GraduationCourseChoices=(('Bachelor of Science','B.Sc.'),
                         ('Bachelor of Engineering, (B.E.)','B.E.'),
                         ('Bachelor of Technology, (B.Tech.)','B.Tech.'),
                         ('Bachelor of Arts, (B.A.)','B.A.'),
                         ('Bachelor of Commerce, (B.Com.)','B.Com.'))


GraduationStreamChoices=(('Information Technology','Information Technology'),
                         ('Computer Science','Computer Science'),
                         ('Mechanical Engg','Mechanical Engg'),
                         ('Electrical Engg','Electrical Engg'),
                         ('Electronics and Communication',
                          'Electronics and Communication'),
                         ('History','History'),
                         ('Geography','Geography'),('Economics','Economics'),
                         ('Physics','Physics'),
                         ('Chemistry','Chemistry'),
                         ('Maths','Maths'))






class PersonalDetails(models.Model):

    user = models.OneToOneField(User)
    name = models.CharField(max_length=20,default="")
    email = models.EmailField()
    contact_no = models.CharField(max_length=13,default="")
    location=models.CharField(max_length=20,default="")


class SecondaryDetails(models.Model):

    user = models.ForeignKey(User, unique=False)
    schoolName = models.CharField(max_length=50,default="")
    board = models.CharField(max_length=20,default="")
    cgpa = models.FloatField(default=0)
    year=models.CharField(max_length=20,default="")

class SeniorSecondaryDetails(models.Model):

    user = models.ForeignKey(User, unique=False)
    schoolName = models.CharField(max_length=50,default="")
    board = models.CharField(max_length=20,default="")
    cgpa = models.FloatField(default=0)
    year=models.CharField(max_length=20,default="")
    stream=models.CharField(max_length=20,choices=SeniorSecondaryChoices)

class GraduationDetails(models.Model):

    user = models.ForeignKey(User, unique=False)
    schoolName = models.CharField(max_length=50,default="")
    board = models.CharField(max_length=20,default="")
    cgpa = models.FloatField(default=0)
    year=models.CharField(max_length=20,default="")
    course=models.CharField(max_length=100,choices=GraduationCourseChoices)
    stream=models.CharField(max_length=100,choices=GraduationStreamChoices)

class Internship(models.Model):#need to edit for multiple Internships
    user = models.ForeignKey(User, unique=False)
    profile = models.CharField(max_length=20, default="")
    organisation = models.CharField(max_length=50, default="")
    duration = models.CharField(max_length=20, default="")
    description=models.CharField(max_length=200, default="")


class Job(models.Model):

    user = models.ForeignKey(User, unique=False)
    profile = models.CharField(max_length=20, default="")
    organisation = models.CharField(max_length=50, default="")
    duration = models.CharField(max_length=20, default="")
    description=models.CharField(max_length=200, default="")


class Skills(models.Model):

    user = models.ForeignKey(User, unique=False)
    skill=models.CharField(max_length=50,default="")


class Projects(models.Model):

    user = models.ForeignKey(User, unique=False)
    Name = models.CharField(max_length=20, default="")
    duration=models.CharField(max_length=20, default="")
    description=models.CharField(max_length=200, default="")



from django import forms
from django.forms import ModelForm,Textarea
from . import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

EducationChoice=('Secondary','Senior Secondary','Graduation','Post Graduation')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.first_name = cleaned_data['first_name']
            user.last_name = cleaned_data['last_name']
            user.email=cleaned_data['email']

            if commit:
                user.save()

            return user


class PersonalForm(ModelForm):
    class Meta:
        model = models.PersonalDetails
        fields = ['name', 'email', 'contact_no', 'location']



class SecondaryForm(ModelForm):
    class Meta:
        model = models.SecondaryDetails
        fields = ['schoolName','board','cgpa','year']
        

class SeniorSecondaryForm(ModelForm):
    class Meta:
        model=models.SeniorSecondaryDetails
        fields=['schoolName','board','cgpa','year','stream']
        

class GraduationForm(ModelForm):
    class Meta:
        model=models.GraduationDetails
        fields=['schoolName','board','cgpa','year','stream','course']
        labels = {
            'schoolName': ('College')
        }
        



class InternshipForm(ModelForm):
    class Meta:
        model=models.Internship
        fields=['profile','organisation','duration','description']
        widgets = {
            'description': Textarea(attrs={'cols': 30, 'rows': 5}),
        }


class SkillsForm(ModelForm):
    class Meta:
        model=models.Skills
        fields=['skill']

        

class JobForm(ModelForm):
    class Meta:
        model=models.Job
        fields=['profile','organisation','duration','description']
        widgets = {
            'description': Textarea(attrs={'cols': 30, 'rows': 5}),
        }

class ProjectForm(ModelForm):
    class Meta:
        model = models.Projects
        fields = [ 'Name','duration', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 30, 'rows': 5}),
        }
        
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
from accounts.forms import *
from accounts.models import *
from django.template import loader, Context
from weasyprint import HTML
from django.core.mail import EmailMessage
from django.forms import modelformset_factory


# Create your views here.
def home(request):

    return render(request,'accounts/home.html')

def register(request):
    if request.method =='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data

            print(data)
            form.save()
            return redirect('/account/login/')
    else:
        form =RegistrationForm()
        args={'form':form}
        return render(request,'accounts/reg_form.html',args)


def personal_details(request):

    try:
        instance=PersonalDetails.objects.get(user=request.user)

    except:
        instance=None

    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=instance)
        if form.is_valid():
            personal = form.save(commit=False)
            personal.user = request.user
            personal.save()
            return redirect("/account/profile")

    else:
        form = PersonalForm(instance=instance)
        args = {'form': form}
        return render(request, 'accounts/personal_form.html', args)



def secondaryDetails(request):

    try:
        instance=SecondaryDetails.objects.get(user=request.user)


    except:
        instance=None

    if request.method =='POST':
        form=SecondaryForm(request.POST,instance=instance)
        if form.is_valid():
            education = form.save(commit=False)
            education.user=request.user
            education.save()

            return redirect("/account/profile/")
    else:
        form =SecondaryForm(instance=instance)
        args={'form':form}
        return render(request,'accounts/secondary.html',args)



def seniorSecondaryDetails(request):

    try:
        instance=SeniorSecondaryDetails.objects.get(user=request.user)

    except:
        instance=None

    if request.method =='POST':
        form=SeniorSecondaryForm(request.POST,instance=instance)
        if form.is_valid():
            education = form.save(commit=False)
            education.user=request.user
            education.save()

            return redirect("/account/profile/")
    else:
        form =SeniorSecondaryForm(instance=instance)
        args={'form':form}
        return render(request,'accounts/senior_secondary.html',args)


def graduationDetails(request):
    try:
        instance=GraduationDetails.objects.get(user=request.user)


    except:
        instance=None
    if request.method =='POST':
        form=GraduationForm(request.POST,instance=instance)
        if form.is_valid():
            education = form.save(commit=False)
            education.user=request.user
            education.save()

            return redirect("/account/profile/")
    else:
        form =GraduationForm(instance=instance)
        args={'form':form}
        return render(request,'accounts/graduation.html',args)



def internshipDetails(request):
    if request.method =='POST':
        form=InternshipForm(request.POST)
        if form.is_valid():
            Internship = form.save(commit=False)
            Internship.user=request.user
            Internship.save()

            return redirect("/account/profile/")
    else:
        form =InternshipForm()
        args={'form':form}
        return render(request,'accounts/internships.html',args)


def jobDetails(request):
    if request.method =='POST':
        form=JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user=request.user
            job.save()

            return redirect("/account/profile/")
    else:
        form =JobForm()
        args={'form':form}
        return render(request,'accounts/jobs.html',args)


def projectDetails(request):
    if request.method =='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user=request.user
            project.save()

            return redirect("/account/profile/")
    else:
        form =ProjectForm()
        args={'form':form}
        return render(request,'accounts/projects.html',args)

def Skill(request):
    if request.method =='POST':
        form=SkillsForm(request.POST)
        if form.is_valid():
            skills = form.save(commit=False)
            skills.user=request.user
            skills.save()

            return redirect("/account/profile/")
    else:
        form =SkillsForm()
        args={'form':form}
        return render(request,'accounts/skills.html',args)




def generatePDF(request):
    args={}
    personalObj = PersonalDetails.objects.get(user = request.user)
    print(personalObj.name)
    args['personalObj'] = personalObj

    if SecondaryDetails.objects.filter(user = request.user):
        secondaryObj = list(SecondaryDetails.objects.filter(user = request.user))
        args['secondaryObj']=secondaryObj

    if SeniorSecondaryDetails.objects.filter(user = request.user):
        ssObj = list(SeniorSecondaryDetails.objects.filter(user = request.user))
        args['ssObj'] = ssObj




    if GraduationDetails.objects.filter(user=request.user):
        graduationObj = list(GraduationDetails.objects.filter(user=request.user))
        args['graduationObj'] = graduationObj


    if Internship.objects.filter(user=request.user):
        internshipObj = list(Internship.objects.filter(user=request.user))
        args['internshipObj']=internshipObj

    if Projects.objects.filter(user=request.user):
        projectsObj = list(Projects.objects.filter(user=request.user))
        args['projectObj'] = projectsObj

    if Job.objects.filter(user=request.user):
        jobObj = list(Job.objects.filter(user=request.user))
        args['jobObj']=jobObj
    if Skills.objects.filter(user=request.user):
        skillsObj = list(Skills.objects.filter(user=request.user))
        args['skillsObj']=skillsObj



    t = loader.get_template('accounts/pdf_template.html')
    c = Context(args)
    rendered = t.render(c)
    rendered = str(rendered)
    html = HTML(string=rendered)
    main_doc = html.render()
    pdf = main_doc.write_pdf()
    return HttpResponse(pdf, content_type='application/pdf')


def chooseTemplate(request):
    return render(request, 'accounts/chooseTemplate.html')




def generatePDF2(request):
    args = {}
    personalObj = PersonalDetails.objects.get(user=request.user)
    print(personalObj.name)
    args['personalObj'] = personalObj

    if SecondaryDetails.objects.filter(user=request.user):
        secondaryObj = list(SecondaryDetails.objects.filter(user=request.user))
        args['secondaryObj'] = secondaryObj

    if SeniorSecondaryDetails.objects.filter(user=request.user):
        ssObj = list(SeniorSecondaryDetails.objects.filter(user=request.user))
        args['ssObj'] = ssObj

    if GraduationDetails.objects.filter(user=request.user):
        graduationObj = list(GraduationDetails.objects.filter(user=request.user))
        args['graduationObj'] = graduationObj

    if Internship.objects.filter(user=request.user):
        internshipObj = list(Internship.objects.filter(user=request.user))
        args['internshipObj'] = internshipObj

    if Projects.objects.filter(user=request.user):
        projectsObj = list(Projects.objects.filter(user=request.user))
        args['projectObj'] = projectsObj

    if Job.objects.filter(user=request.user):
        jobObj = list(Job.objects.filter(user=request.user))
        args['jobObj'] = jobObj
    if Skills.objects.filter(user=request.user):
        skillsObj = list(Skills.objects.filter(user=request.user))
        args['skillsObj'] = skillsObj

    t = loader.get_template('accounts/pdf_template2.html')
    c = Context(args)
    rendered = t.render(c)
    rendered = str(rendered)
    html = HTML(string=rendered)
    main_doc = html.render()
    pdf = main_doc.write_pdf()
    return HttpResponse(pdf, content_type='application/pdf')



def editInternships(request):
    InternshipFormSet = modelformset_factory(Internship, form=InternshipForm, can_delete=True)
    qset = Internship.objects.filter(user=request.user)
    formset = InternshipFormSet(queryset=qset)
    if request.method == 'POST':


        formset = InternshipFormSet(request.POST)
        if formset.is_valid():

            instances = formset.save(commit=False)

            for instance in instances:
                instance.user = request.user
                instance.save()

            for obj in formset.deleted_objects:
                obj.delete()
        return redirect("/account/profile")

    args = {'formset': formset,

            }

    return render(request, 'accounts/edit_internship.html', args)



def editProjects(request):

    ProjectFormSet = modelformset_factory(Projects, form=ProjectForm,can_delete=True)
    qset = Projects.objects.filter(user=request.user)
    formset = ProjectFormSet(queryset=qset)
    if request.method == 'POST':

        formset = ProjectFormSet(request.POST)
        if formset.is_valid():

            instances=formset.save(commit=False)
            for instance in instances:
                instance.user=request.user
                instance.save()

        for obj in formset.deleted_objects:
            obj.delete()
        return  redirect("/account/profile")

    args = {'formset': formset,

                    }

    return render(request,'accounts/edit_projects.html', args)

def editSkills(request):

    SkillsFormSet = modelformset_factory(Skills, form=SkillsForm,can_delete=True)
    qset = Skills.objects.filter(user=request.user)
    formset = SkillsFormSet(queryset=qset)
    if request.method == 'POST':

        formset = SkillsFormSet(request.POST)
        if formset.is_valid():

            instances=formset.save(commit=False)
            for instance in instances:
                instance.user=request.user
                instance.save()

        for obj in formset.deleted_objects:
            obj.delete()
        return  redirect("/account/profile")

    args = {'formset': formset,

                    }

    return render(request,'accounts/edit_skills.html', args)




def editJobs(request):
    JobFormSet = modelformset_factory(Job, form=JobForm,can_delete=True)
    qset = Job.objects.filter(user=request.user) # or however your getting your Points to modify
    formset = JobFormSet(queryset=qset)
    if request.method == 'POST':
        # deal with posting the data
        formset = JobFormSet(request.POST)
        if formset.is_valid():
            # if it is not valid then the "errors" will fall through and be returned
            instances=formset.save(commit=False)
            for instance in instances:
                instance.user=request.user
                instance.save()

            for obj in formset.deleted_objects:
                obj.delete()

        return  redirect("/account/profile")# to your redirect

    args = {'formset': formset,

                    }

    return render(request,'accounts/edit_jobs.html', args)


def personal_profile(request):
    args={}
    personalObj = PersonalDetails.objects.get(user = request.user)
    print(personalObj.name)
    args['personalObj'] = personalObj

    if SecondaryDetails.objects.filter(user = request.user):
        secondaryObj = list(SecondaryDetails.objects.filter(user = request.user))
        args['secondaryObj']=secondaryObj

    if SeniorSecondaryDetails.objects.filter(user = request.user):
        ssObj = list(SeniorSecondaryDetails.objects.filter(user = request.user))
        args['ssObj'] = ssObj




    if GraduationDetails.objects.filter(user=request.user):
        graduationObj = list(GraduationDetails.objects.filter(user=request.user))
        args['graduationObj'] = graduationObj


    if Internship.objects.filter(user=request.user):
        internshipObj = list(Internship.objects.filter(user=request.user))
        args['internshipObj']=internshipObj

    if Projects.objects.filter(user=request.user):
        projectsObj = list(Projects.objects.filter(user=request.user))
        args['projectObj'] = projectsObj

    if Job.objects.filter(user=request.user):
        jobObj = list(Job.objects.filter(user=request.user))
        args['jobObj']=jobObj

    if Skills.objects.filter(user=request.user):
        skillsObj = list(Skills.objects.filter(user=request.user))
        args['skillsObj']=skillsObj

    t = loader.get_template('accounts/personal_details.html')
    c = Context(args)
    rendered = t.render(c)



    return HttpResponse(rendered)





def sendEmail(request):

    args = {}
    personalObj = PersonalDetails.objects.get(user=request.user)
    print(personalObj.name)
    args['personalObj'] = personalObj

    if SecondaryDetails.objects.filter(user=request.user):
        secondaryObj = list(SecondaryDetails.objects.filter(user=request.user))
        args['secondaryObj'] = secondaryObj

    if SeniorSecondaryDetails.objects.filter(user=request.user):
        ssObj = list(SeniorSecondaryDetails.objects.filter(user=request.user))
        args['ssObj'] = ssObj

    if GraduationDetails.objects.filter(user=request.user):
        graduationObj = list(GraduationDetails.objects.filter(user=request.user))
        args['graduationObj'] = graduationObj

    if Internship.objects.filter(user=request.user):
        internshipObj = list(Internship.objects.filter(user=request.user))
        args['internshipObj'] = internshipObj

    if Projects.objects.filter(user=request.user):
        projectsObj = list(Projects.objects.filter(user=request.user))
        args['projectObj'] = projectsObj

    if Job.objects.filter(user=request.user):
        jobObj = list(Job.objects.filter(user=request.user))
        args['jobObj'] = jobObj

    t = loader.get_template('accounts/pdf_template.html')
    c = Context(args)
    rendered = t.render(c)
    rendered = str(rendered)
    html = HTML(string=rendered)
    main_doc = html.render()
    pdf = main_doc.write_pdf()


    email = EmailMessage('Resume', 'hello','Anurag Harsh' , to=[request.user.email])
    try:

        email.attach('Resume',pdf,'application/pdf')
        email.send()
        return HttpResponse("E-Mail Sent Successfuly")
    except:
        return HttpResponse("Error Occured")




def logout_view(request):
    logout(request)

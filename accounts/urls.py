from django.conf.urls import url

from . import views
from django.contrib.auth.views import login,logout
urlpatterns = [
    url(r'^$',views.home),
    url(r'^base/$',views.base),
    url(r'^login/$',login,{'template_name':'accounts/login.html'}),
    url(r'^logout/$',logout,{'template_name':'accounts/logout.html'}),
    url(r'^register/$',views.register,name='register'),
    url(r'^personal/$',views.personal_details),
    url(r'^profile/$',views.personal_profile),
    url(r'^secondary/$',views.secondaryDetails),
    url(r'^senior_secondary/$',views.seniorSecondaryDetails),
    url(r'^graduation/$',views.graduationDetails),
    url(r'^internships/$',views.internshipDetails),
    url(r'^jobs/$',views.jobDetails),
    url(r'^projects/$',views.projectDetails),
    url(r'^generate/$',views.chooseTemplate),
    url(r'^temp1/$',views.generatePDF),
    url(r'^temp2/$',views.generatePDF2),
    url(r'^edit_skills/$',views.editSkills),
    url(r'^skills/$',views.Skill),
    url(r'^mail_1/$', views.sendEmail_1),
    url(r'^mail_2/$', views.sendEmail_2),
    url(r'^edit_jobs/$',views.editJobs),
    url(r'^edit_projects/$',views.editProjects),
    url(r'^edit_internships/$',views.editInternships),
    url(r'^logout/$',views.logout_view),

]

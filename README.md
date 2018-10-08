# online-cv-builder
Online CV Builder is an application that simplifies the task of creating a CV for individuals. The system is flexible to be used and reduces the need of thinking and designing an appropriate CV according to qualifications. The system is developed to provide an easy means for creating a professional looking CV. Individuals just have to fill up a form that specifies questions from all required fields such as personal details, educational details, projects,internships, skills and so on. The answers provided by the users are stored and the system automatically generates a well structured CV. Users have option to download CV in PDF format or receive on registered email address.


It uses Django, a free and open-source web framework, written in Python, which follows the model-view-template (MVT) architectural pattern.

Installation Instructions
	
Prerequisites to run Online CV Builder on local machine consist of  Python3 and git . Although Online CV Builder is a web application, one can still run it locally using following instructions:

a) . Use git clone to clone this repository to your local machine: 

`$ git clone https://github.com/anurag-bug/online-cv-builder.git`

b.)  Change current directory

`$ cd online-cv-builder`

c.)  Create virtual environment 

`$ python3 -m venv myvenv`

d.)  Activate virtual environment 

`$ source myvenv/bin/activate`

e.) Install Django

`$ pip install django~=1.10.7`

f.) Install WeasyPrint

`$ pip install weasyprint`

g.) In settings.py file set `EMAIL_HOST_USER` and                
`EMAIL_HOST_PASSWORD`.

g.) Run Server

`$ python manage.py runserver`

App will run on http://127.0.0.1:8000

This web app is also hosted at http://anurag3feb.pythonanywhere.com 

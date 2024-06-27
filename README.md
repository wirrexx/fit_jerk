# Fit Bastard

## Overview

The different fitness app. Fit Bastard is here to help you loose weight, gain muscles or tone down. 
It will give you a coach that pushes you beyond your levels. Fit Bastard has three prepared workout 
plans that depend on your goals. 

## TechStack:

Languages: 
- Python 
- HTML 
- CSS

Frameworks
- Django
- django-allauth

Databases: 
- Development: [Sqlite3](https://sqlite.org/)

Hosting: 
- Pythonanywhere

## Installation instructions

```
# Clone this repo! 
git clone git@github.com:wirrexx/fit_jerk.git

# In the directory where .git resides create a virtual environment
python -m venv .venv

# install requirements from requirements.txt
pip install -r requirements.txt

# change directory to fj/
cd fj/

# migrate and makemigrations
python manage.py makemigrations
python manage.py migrate

# create .env file
touch .env

# populate this file with a secret key
SECRET_KEY=YOUR_SECRET_KEY

#Note: google auth will not work without you specifying a GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET
#+     for detailed instructions on how to setup google auth see: DOCs/HOWTO_google_auth
#Note: The email backend is configured to send emails to the console. If you want to be able to use
#+     EMAIL via gmail, refer to: DOCs/HOWTO_google_auth
```

## Implemented Features 

- Authenticication System
	[Logout, Login, ChangePassword, ResetPassword, Signup, OAuth with Google]
- Profile
	[BMI, weight, height, progress, picture, completion posts, choose exercise, avatar]
- Workouts
	[Exercises: Loose, Muscles, ToneDown, Timer, Start, Pause, Give up, Resume, Finish, embedded Youtube videos] 
	

## Expected Features

- Online Shop
- AI driven Feedback
- Statistics
- Migrate to Google Playstore

## Roles

Ana Pereira - Team Manager/Frontend/Backend
Christian Peter - Technical Leader/Code Quality/Backend
Wisam Odish - Lead Developer/Frontend/Backend

## General Planning

We are, and we can't stress this enough, a team!
Don't be afraid to ask for help!
We use github project:


[Project](https://github.com/users/wirrexx/projects/1/views/7)

	
Standups at 9.00am












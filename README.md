# Fit Bastard

## Overview

The different fitness app. Fit Bastard is here to help you loose weight, gain muscles or tone down. 
It will give you a coach that pushes you beyond your levels. Fit Bastard has three prepared workout 
plans that depend on your goals. 

## Technology used:

Languages: 
	- Python 
 	- HTML 
  	- CSS
Webframework: [Django](https://www.djangoproject.com/)
Database: 
	- Development: [Sqlite3](https://sqlite.org/)
 	- Production: [Postgresql](https://www.postgresql.org/)
Hosting: [pythonanywhere](https://www.pythonanywhere.com/) 
	


## Features 

- Sign Up
	- user name
	- weight
	- hight
	- email 
	- password
	- What are your goals? 
		loose weight -> be very rude about it
		gain muscle -> be politely rude about it
		stay the same -> why are you using this app? 

	-> Backend sends confirmation email, redirect to login?

- Login
	- Landing page
		greetings User
		trainingplan based on your goals
		Start workout now -> button

- Do workout 
	Start -> Countdown starts 
	Pause/Resume workout -> button 
	Automatic finish -> redirect to landing page

- Progress tracker
	- Audio confirmation: "Hey! You did it! Great job!
	- automatic blogpost on users landing page

- Logout 
	

## Nice to have

- Create an Avatar
- Continue with workout -> button on landing page
- Automatic posts on twitter/linkedIn
- Audio 
- Oauth
- AppStore Implementationn
- Host our own server

## User Story

Landing Page (Profile) -> Start Workout -> Workout starts -> Finish -> Landing Page  
		|								|			
												-----> Pause --> Restart --- Finish

## Questions

How do workout messages get created? 
	-> Prewritten messages
	-> ChatGPT generates message

## Roles

Product Owner (Ana)
Lead Developer (Wisam)
Head of Operation (Christian)

## General Planning

We are, and I can't stress this enough, a team!
Don't be afraid to ask for help!
We use github project:

[Project](https://github.com/users/wirrexx/projects/1/views/7)
	
Standups at 9.00am












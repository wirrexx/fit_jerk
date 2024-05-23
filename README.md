# fit_jerk

## Overview

A rude fitness app. 
Fit Jerk is here to help you loose weight, gain muscles or tone down. It will give you an coach that pushes you beyond your levels. Fit jerk has three prepared workout plans that depend on your goals. 

## Resources:

[Django Testing](https://docs.djangoproject.com/en/5.0/intro/tutorial05/)

## Technology used:

Implementation will be done with 
	Django
	Development:
		Sqlite
	Production 
		Postgresql 
	CSS
	
	Hosting:
		AWS -> nope, hidden costs!
		Google -> nope, suckers in data collection!
		Pythonanywhere -> Easy to use at least for development

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
	- Audio confirmation "Hey, you fat bastard, you did it"
	- automatic blogpost

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
	Survey to generate ideas

Lead Developer (Wisam)
	

Head of Operation (Christian)
	


## General Planning

We are, and I can't stress this enough, a team!
Don't be afraid to ask for help!
We use github project:

[Project](https://github.com/users/wirrexx/projects/1/views/7)
	

- Standup at 9.00am












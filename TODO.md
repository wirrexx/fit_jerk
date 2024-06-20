## TODO

1. Checkout Oauth [x]

1.1 Implement Google OAuth [x]
1.2. Stylize login.html
	-> templates/socialaccount
1.3. Change CLIENT_ID and CLIENT_SECRET in google console

2. Deploy to python anywhere
3. Write Tests
4. Write documentation


DEADLINE: 19.06 for testingphase

<hr>


## DRY!!!!

Save BMI in database [x]

## Admin Panel
	Register Profile and connect it to User

## Implement Argon2 [x]

Documentation:

[Resource: Django documentation](https://docs.djangoproject.com/en/5.0/topics/auth/passwords/)

```sh
# install argon2-cffi package
pip install argon2-cffi

# safe to requirements.txt
pip freeze > requirements.txt
```
Add to settings: 
PASSWORD_HASHERS = 
	["django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

## Implement OAuth
	Google
	
## Tests
	Write tests for views, functions etc..

## Password Reset
	Force HTTPS
	Customize: registration/custom_password_reset_email.html
	nice to have: function based approach
	def password_reset_viev(request):
 	   token_generator = PasswordResetTokenGenerator()
  	   token = token_generator.make_token()

## Signup
	Handle Error messages
	finish cleaning functions
	Rename FitUserForm in forms.py

## Research
	APIs
	Django REST Framework
	Code:
	```python
	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
    	if created:
    	    Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
	    instance.profile.save()
	```

## Functionality
	Add a Stop workout button
	Add automatic generation of posts with LLM -> integrate ChatBot
	Add Footer: 
		Imprint
		Copyright
		About

## Style
	Add favicon

## Documentation
	Add docstrings
	HOWTO Blogposts
		LoginView
		LogoutView
		SignupForm
		PasswordReset 
		CustomUser
		using dotenv
		Deployment

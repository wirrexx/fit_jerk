## TODO

1. Refactor code and improve code quality
2. Deploy to python anywhere
3. Write Tests
4. Write documentation
5. Admin Panel: Register Profile and connect it to User
6. Research
7. Handle statics

```python
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
```

## Documentation
	HOWTO Blogposts
		LoginView
		LogoutView
		SignupForm
		PasswordReset 
		CustomUser
		using dotenv
		Deployment
		Implementation of OAuth

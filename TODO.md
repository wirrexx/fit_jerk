### All

Fill with content
    Imprint
    Privacy Policy
Upload/Create Logo
Git Tutorial

### Xtn

1. Refactor code and improve code quality:
	DRY!
 	make code self documenting
	add docstrings
	refactor code
	Remove dead code
3. Write Tests
4. Deploy to python anywhere
5. Write documentation
6. Admin Panel: Register Profile and connect it to User
7. Research:

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

## Prospects

- Chat between members
- E-commerce
- Nutrician plan
- Personalized trainnings
- AI-driven feedback

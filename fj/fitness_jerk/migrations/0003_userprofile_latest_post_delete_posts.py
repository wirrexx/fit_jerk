# Generated by Django 5.0.6 on 2024-06-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_jerk', '0002_rename_members_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='latest_post',
            field=models.CharField(default='Welcome! You finally choose to better yourself!', max_length=100),
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]

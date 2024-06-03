# Generated by Django 5.0.6 on 2024-05-31 03:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitbastards', '0007_members_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='post',
        ),
        migrations.AddField(
            model_name='posts',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fitbastards.members'),
            preserve_default=False,
        ),
    ]

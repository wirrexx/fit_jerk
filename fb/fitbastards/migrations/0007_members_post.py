# Generated by Django 5.0.6 on 2024-05-31 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitbastards', '0006_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='post',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

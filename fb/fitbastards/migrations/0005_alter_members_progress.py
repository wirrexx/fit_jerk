# Generated by Django 5.0.6 on 2024-05-31 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitbastards', '0004_alter_members_height_alter_members_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]

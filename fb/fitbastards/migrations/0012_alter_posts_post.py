# Generated by Django 5.0.6 on 2024-05-31 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitbastards', '0011_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post',
            field=models.CharField(default='Welcome', max_length=255),
        ),
    ]

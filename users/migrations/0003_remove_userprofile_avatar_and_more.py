# Generated by Django 5.1.2 on 2024-10-22 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_completed_levels_userprofile_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='completed_levels',
        ),
    ]

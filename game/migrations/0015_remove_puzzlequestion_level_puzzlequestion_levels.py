# Generated by Django 5.1.2 on 2024-11-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_alter_level_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puzzlequestion',
            name='level',
        ),
        migrations.AddField(
            model_name='puzzlequestion',
            name='levels',
            field=models.ManyToManyField(related_name='questions', to='game.level'),
        ),
    ]

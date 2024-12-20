# Generated by Django 5.1.2 on 2024-11-22 12:23

import game.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_remove_puzzlequestion_levels_gamelevel_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamelevel',
            name='level',
        ),
        migrations.RemoveField(
            model_name='level',
            name='name',
        ),
        migrations.RemoveField(
            model_name='puzzlepiece',
            name='number',
        ),
        migrations.RemoveField(
            model_name='puzzlequestion',
            name='level',
        ),
        migrations.AddField(
            model_name='puzzlequestion',
            name='levels',
            field=models.ManyToManyField(related_name='questions', to='game.level'),
        ),
        migrations.AlterField(
            model_name='level',
            name='correct_answer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='level',
            name='description',
            field=models.TextField(default='Default description'),
        ),
        migrations.AlterField(
            model_name='level',
            name='image',
            field=models.ImageField(default='puzzle_pieces/default_image.png', upload_to='puzzle_pieces/'),
        ),
        migrations.AlterField(
            model_name='level',
            name='number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='puzzlepiece',
            name='image',
            field=models.ImageField(upload_to=game.models.puzzle_piece_upload_path),
        ),
        migrations.AlterField(
            model_name='puzzlequestion',
            name='question_text',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_level_piece_height_level_piece_width'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['number']},
        ),
        migrations.AddField(
            model_name='puzzlepiece',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='level',
            name='number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
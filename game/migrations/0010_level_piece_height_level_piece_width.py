# Generated by Django 5.1.2 on 2024-11-17 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_puzzle_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='piece_height',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='level',
            name='piece_width',
            field=models.IntegerField(default=100),
        ),
    ]
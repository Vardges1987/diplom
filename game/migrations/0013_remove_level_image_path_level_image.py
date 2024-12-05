# Generated by Django 5.1.2 on 2024-11-20 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_level_image_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='image_path',
        ),
        migrations.AddField(
            model_name='level',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='levels_images/'),
        ),
    ]

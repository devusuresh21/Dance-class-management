# Generated by Django 4.1.2 on 2023-05-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('danceapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='dance',
            field=models.ManyToManyField(to='danceapp.category'),
        ),
    ]

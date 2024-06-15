# Generated by Django 5.0.6 on 2024-06-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='head',
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.ManyToManyField(related_name='body', to='blog.body'),
        ),
        migrations.AddField(
            model_name='blog',
            name='head',
            field=models.ManyToManyField(related_name='heading', to='blog.heading'),
        ),
    ]
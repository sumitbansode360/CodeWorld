# Generated by Django 5.0.6 on 2024-06-15 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='like',
        ),
    ]

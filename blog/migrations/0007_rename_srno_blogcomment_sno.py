# Generated by Django 5.0.6 on 2024-06-09 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='SrNo',
            new_name='sno',
        ),
    ]
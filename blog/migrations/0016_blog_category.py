# Generated by Django 5.0.6 on 2024-06-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_delete_userblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('tech', 'Tech'), ('gaming', 'Gaming'), ('ai', 'AI'), ('elec', 'Electroincs')], default='', max_length=200),
            preserve_default=False,
        ),
    ]

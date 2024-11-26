# Generated by Django 4.2.4 on 2024-06-22 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

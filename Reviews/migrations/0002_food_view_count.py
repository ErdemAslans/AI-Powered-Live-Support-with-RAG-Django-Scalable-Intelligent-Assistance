# Generated by Django 4.2.4 on 2024-06-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='view_count',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]

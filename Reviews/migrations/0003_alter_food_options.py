# Generated by Django 4.2.4 on 2024-06-19 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0002_food_view_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ('title',)},
        ),
    ]

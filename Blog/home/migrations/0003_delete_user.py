# Generated by Django 5.0.6 on 2024-05-13 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.1 on 2022-08-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_studymatirial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_views',
            field=models.BigIntegerField(default=0),
        ),
    ]

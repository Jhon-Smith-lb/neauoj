# Generated by Django 3.1 on 2020-08-14 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ojauth', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Signin',
        ),
        migrations.DeleteModel(
            name='Signinlog',
        ),
    ]

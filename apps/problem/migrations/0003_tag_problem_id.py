# Generated by Django 3.1 on 2020-08-16 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='problem_id',
            field=models.CharField(default=12, max_length=48),
            preserve_default=False,
        ),
    ]

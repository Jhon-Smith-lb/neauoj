# Generated by Django 3.1 on 2020-08-27 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0002_auto_20200827_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='memory',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='pass_rate',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='time',
            field=models.IntegerField(null=True),
        ),
    ]
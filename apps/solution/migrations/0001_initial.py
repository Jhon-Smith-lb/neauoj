# Generated by Django 3.1 on 2020-08-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compileinfo',
            fields=[
                ('solution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('error', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'compileinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Runtimeinfo',
            fields=[
                ('solution_id', models.IntegerField(primary_key=True, serialize=False)),
                ('error', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'runtimeinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('solution_id', models.AutoField(primary_key=True, serialize=False)),
                ('problem_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=48)),
                ('nick', models.CharField(max_length=20)),
                ('time', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('in_date', models.DateTimeField()),
                ('result', models.SmallIntegerField()),
                ('language', models.PositiveIntegerField()),
                ('ip', models.CharField(max_length=46)),
                ('contest_id', models.IntegerField(blank=True, null=True)),
                ('valid', models.IntegerField()),
                ('num', models.IntegerField()),
                ('code_length', models.IntegerField()),
                ('judgetime', models.DateTimeField(blank=True, null=True)),
                ('pass_rate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('lint_error', models.PositiveIntegerField()),
                ('judger', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'solution',
                'managed': False,
            },
        ),
    ]

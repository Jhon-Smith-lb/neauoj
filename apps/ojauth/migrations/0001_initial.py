# Generated by Django 3.1 on 2020-08-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loginlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=48)),
                ('password', models.CharField(blank=True, max_length=40, null=True)),
                ('ip', models.CharField(blank=True, max_length=46, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'loginlog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('in_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'signin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Signinlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signinid', models.IntegerField()),
                ('user_id', models.CharField(max_length=48)),
                ('room', models.CharField(blank=True, max_length=60, null=True)),
                ('status', models.CharField(max_length=1)),
                ('in_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'signinlog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.CharField(max_length=48, primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('submit', models.IntegerField(blank=True, null=True)),
                ('solved', models.IntegerField(blank=True, null=True)),
                ('defunct', models.CharField(max_length=1)),
                ('ip', models.CharField(max_length=46)),
                ('accesstime', models.DateTimeField(blank=True, null=True)),
                ('volume', models.IntegerField()),
                ('language', models.IntegerField()),
                ('password', models.CharField(blank=True, max_length=32, null=True)),
                ('reg_time', models.DateTimeField(blank=True, null=True)),
                ('nick', models.CharField(max_length=20, unique=True)),
                ('school', models.CharField(max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
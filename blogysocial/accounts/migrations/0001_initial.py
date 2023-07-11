# Generated by Django 4.2 on 2023-07-11 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('email', models.CharField(max_length=150, unique=True, verbose_name='Email Address')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('password', models.CharField(max_length=150, verbose_name='Password')),
                ('phone', models.CharField(blank=True, max_length=35, null=True, verbose_name='Phone Number')),
                ('photo', models.ImageField(blank=True, default='images/default.png', help_text='Upload photo', null=True, upload_to='images/authors/', verbose_name='Author Photo')),
                ('about_me', models.TextField(blank=True, max_length=255, null=True, verbose_name='About me')),
                ('web', models.CharField(blank=True, max_length=255, null=True, verbose_name='Author Website')),
                ('instagram', models.CharField(blank=True, max_length=255, null=True, verbose_name='Author Instagram')),
                ('twitter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Author Twitter')),
                ('remember_me', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
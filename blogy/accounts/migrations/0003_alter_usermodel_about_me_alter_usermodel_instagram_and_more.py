# Generated by Django 4.2 on 2023-07-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_usermodel_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='about_me',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='About me'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='instagram',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Author Instagram'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='phone',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='photo',
            field=models.ImageField(blank=True, default='images/default.png', help_text='Upload photo', null=True, upload_to='images/authors/', verbose_name='Author Photo'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='twitter',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Author Twitter'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='web',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Author Website'),
        ),
    ]
# Generated by Django 4.2 on 2023-04-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_article_title_alter_comment_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_featured',
            field=models.BooleanField(default=False, help_text='Change make article appear on index page', verbose_name='Make article appear on index page'),
        ),
    ]
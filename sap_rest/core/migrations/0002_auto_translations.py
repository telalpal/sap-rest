# Generated by Django 2.2.2 on 2019-06-17 21:37

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='title_de',
            field=models.CharField(max_length=255, null=True, verbose_name='Title of Folder'),
        ),
        migrations.AddField(
            model_name='folder',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Title of Folder'),
        ),
        migrations.AddField(
            model_name='question',
            name='text_de',
            field=models.TextField(null=True, verbose_name='Text of Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Text of Question'),
        ),
        migrations.AddField(
            model_name='resource',
            name='body_de',
            field=markdownx.models.MarkdownxField(null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='body_en',
            field=markdownx.models.MarkdownxField(null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='title_de',
            field=models.CharField(max_length=255, null=True, verbose_name='Title of Resource'),
        ),
        migrations.AddField(
            model_name='resource',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Title of Resource'),
        ),
    ]

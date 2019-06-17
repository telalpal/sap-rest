# Generated by Django 2.2.2 on 2019-06-17 22:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import sap_rest.core.models.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title of Folder')),
            ],
            options={
                'abstract': False,
            },
            bases=(sap_rest.core.models.mixins.GetTranslationsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of Icon')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title of Template')),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Folder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title of Resource')),
                ('body', ckeditor.fields.RichTextField()),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Folder')),
            ],
            options={
                'abstract': False,
            },
            bases=(sap_rest.core.models.mixins.GetTranslationsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text of Question')),
                ('qtype', models.IntegerField(choices=[(1, 'text'), (2, 'textarea'), (3, 'Maybe relevant'), (4, 'Relevant'), (5, 'Leading candidate')], default=1, verbose_name='Type of Question')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Template')),
            ],
            options={
                'abstract': False,
            },
            bases=(sap_rest.core.models.mixins.GetTranslationsMixin, models.Model),
        ),
        migrations.AddField(
            model_name='folder',
            name='icon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Icon'),
        ),
    ]

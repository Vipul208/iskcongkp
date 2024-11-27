# Generated by Django 5.1.3 on 2024-11-18 03:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(default='', editable=False, max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('date', models.DateField()),
                ('apply_link', models.URLField(blank=True, default='', null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]

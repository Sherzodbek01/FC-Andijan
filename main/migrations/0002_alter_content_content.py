# Generated by Django 4.1.6 on 2023-07-04 12:30

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]

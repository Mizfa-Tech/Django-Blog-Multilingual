# Generated by Django 4.1.2 on 2022-10-30 12:15

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_status_en_remove_post_status_fa'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent_category_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='blog.category', verbose_name='parent category'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent_category_fa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='blog.category', verbose_name='parent category'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=350, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_fa',
            field=models.CharField(max_length=350, null=True, verbose_name='title'),
        ),
    ]

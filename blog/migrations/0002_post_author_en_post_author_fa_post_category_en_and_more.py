# Generated by Django 4.1.2 on 2022-10-30 07:08

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_posts', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='post',
            name='author_fa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_posts', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='post',
            name='category_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='post',
            name='category_fa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at_en',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at_fa',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at_jalali_en',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='created at jalali'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at_jalali_fa',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, null=True, verbose_name='created at jalali'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='meta description'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_description_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='meta description'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_title_en',
            field=models.CharField(blank=True, max_length=320, null=True, verbose_name='meta title'),
        ),
        migrations.AddField(
            model_name='post',
            name='meta_title_fa',
            field=models.CharField(blank=True, max_length=320, null=True, verbose_name='meta title'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_en',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug_fa',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='post',
            name='status_en',
            field=models.CharField(choices=[('PU', 'Publish'), ('IN', 'Inriview'), ('PE', 'Pending')], default='PE', max_length=2, null=True, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='post',
            name='status_fa',
            field=models.CharField(choices=[('PU', 'Publish'), ('IN', 'Inriview'), ('PE', 'Pending')], default='PE', max_length=2, null=True, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail_alt_en',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='thumbnail alt'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail_alt_fa',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='thumbnail alt'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail_en',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/2022/10', verbose_name='thumbnail'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail_fa',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/2022/10', verbose_name='thumbnail'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=350, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_fa',
            field=models.CharField(max_length=350, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at_en',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at_fa',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at_jalali_en',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='updated at jalali'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at_jalali_fa',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, null=True, verbose_name='updated at jalali'),
        ),
    ]

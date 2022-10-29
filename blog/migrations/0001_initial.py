# Generated by Django 4.1.2 on 2022-10-29 14:24

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('created_at_jalali', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='created at jalali')),
                ('updated_at_jalali', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='updated at jalali')),
                ('meta_title', models.CharField(blank=True, max_length=320, null=True, verbose_name='meta title')),
                ('meta_description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='meta description')),
                ('status', models.CharField(choices=[('PU', 'Publish'), ('IN', 'Inriview'), ('PE', 'Pending')], default='PE', max_length=2, verbose_name='status')),
                ('title', models.CharField(max_length=350, verbose_name='title')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='taxonomy/thumbnails/2022/10', verbose_name='thumbnail')),
                ('thumbnail_alt', models.CharField(blank=True, max_length=350, verbose_name='thumbnail alt')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='blog.category', verbose_name='parent category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('created_at_jalali', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='created at jalali')),
                ('updated_at_jalali', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='updated at jalali')),
                ('meta_title', models.CharField(blank=True, max_length=320, null=True, verbose_name='meta title')),
                ('meta_description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='meta description')),
                ('status', models.CharField(choices=[('PU', 'Publish'), ('IN', 'Inriview'), ('PE', 'Pending')], default='PE', max_length=2, verbose_name='status')),
                ('title', models.CharField(max_length=350, verbose_name='title')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/2022/10', verbose_name='thumbnail')),
                ('thumbnail_alt', models.CharField(blank=True, max_length=350, verbose_name='thumbnail alt')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_posts', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
# Generated by Django 4.1.2 on 2022-11-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_is_active_post_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_active_en',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='category',
            name='is_active_fa',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_active_en',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_active_fa',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
    ]

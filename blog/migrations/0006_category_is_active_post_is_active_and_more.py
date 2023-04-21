# Generated by Django 4.1.2 on 2022-11-01 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_description_en_category_description_fa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
        migrations.AlterField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='taxonomy/thumbnails/2022/11', verbose_name='thumbnail'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/2022/11', verbose_name='thumbnail'),
        ),
    ]
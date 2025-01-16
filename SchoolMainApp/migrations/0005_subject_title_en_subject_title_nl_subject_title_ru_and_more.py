# Generated by Django 4.2.17 on 2025-01-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolMainApp', '0004_subject_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='title_nl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='first_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='first_name_nl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='first_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name_nl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='middle_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='middle_name_nl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='middle_name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
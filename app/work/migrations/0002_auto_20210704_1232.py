# Generated by Django 3.2.5 on 2021-07-04 12:32

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path=pathlib.PurePosixPath('/home/kalo/public_html/deploy/app/static/img')),
        ),
        migrations.AlterField(
            model_name='project',
            name='place',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=44),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-03 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(path='/home/kalo/public_html/deploy/static/img'),
        ),
    ]

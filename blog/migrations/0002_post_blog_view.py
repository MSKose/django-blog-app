# Generated by Django 4.1.1 on 2022-09-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_view',
            field=models.IntegerField(default=0),
        ),
    ]

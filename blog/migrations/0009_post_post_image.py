# Generated by Django 4.1.1 on 2022-09-11 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='blog_default.jpg', upload_to='blog_pics'),
        ),
    ]

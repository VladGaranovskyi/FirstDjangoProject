# Generated by Django 4.1.7 on 2023-06-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_alter_comment_author_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, to='postapp.comment'),
        ),
    ]

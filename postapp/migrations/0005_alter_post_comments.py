# Generated by Django 4.1.7 on 2023-06-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0004_alter_post_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='postapp.comment'),
        ),
    ]
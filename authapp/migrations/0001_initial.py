# Generated by Django 4.1.7 on 2023-06-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

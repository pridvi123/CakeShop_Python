# Generated by Django 4.2.5 on 2024-03-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]

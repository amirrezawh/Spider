# Generated by Django 3.2.3 on 2021-06-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registeration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
    ]
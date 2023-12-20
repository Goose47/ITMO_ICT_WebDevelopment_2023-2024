# Generated by Django 4.2.6 on 2023-10-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owners',
            field=models.ManyToManyField(through='blog.CarOwnership', to='blog.owner'),
        ),
        migrations.AddField(
            model_name='owner',
            name='cars',
            field=models.ManyToManyField(through='blog.CarOwnership', to='blog.car'),
        ),
    ]
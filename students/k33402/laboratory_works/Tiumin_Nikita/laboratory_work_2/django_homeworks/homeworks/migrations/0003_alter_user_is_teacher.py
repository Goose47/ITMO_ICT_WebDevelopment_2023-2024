# Generated by Django 4.2.6 on 2023-10-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0002_alter_user_is_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False),
        ),
    ]

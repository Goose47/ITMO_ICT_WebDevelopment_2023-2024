# Generated by Django 5.0 on 2023-12-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musec_app', '0004_alter_userprofile_patronymic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='extension',
        ),
        migrations.RemoveField(
            model_name='file',
            name='path',
        ),
        migrations.RemoveField(
            model_name='file',
            name='type',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default='', upload_to='storage/'),
            preserve_default=False,
        ),
    ]

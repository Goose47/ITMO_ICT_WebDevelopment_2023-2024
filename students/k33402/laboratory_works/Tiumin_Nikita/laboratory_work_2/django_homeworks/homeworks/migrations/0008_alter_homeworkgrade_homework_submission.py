# Generated by Django 4.2.6 on 2023-10-28 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0007_remove_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworkgrade',
            name='homework_submission',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homeworks.homeworksubmission'),
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='postal',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='aboutme',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-05 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

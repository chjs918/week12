# Generated by Django 3.2.5 on 2021-08-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dramaboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drama',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='drama/'),
        ),
    ]

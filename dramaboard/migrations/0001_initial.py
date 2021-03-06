# Generated by Django 3.2.6 on 2021-08-22 16:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('score', models.TextField(choices=[('★', '★'), ('★★', '★★'), ('★★★', '★★★'), ('★★★★', '★★★★'), ('★★★★★', '★★★★★')])),
                ('writer', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='mara/')),
                ('like', models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

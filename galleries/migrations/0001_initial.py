# Generated by Django 3.2.4 on 2021-06-08 11:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('image_url', models.TextField()),
                ('caption', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

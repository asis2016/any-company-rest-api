# Generated by Django 3.2.4 on 2021-06-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(max_length=20),
        ),
    ]

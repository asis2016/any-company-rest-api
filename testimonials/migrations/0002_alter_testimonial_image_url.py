# Generated by Django 3.2.4 on 2021-06-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image_url',
            field=models.TextField(),
        ),
    ]

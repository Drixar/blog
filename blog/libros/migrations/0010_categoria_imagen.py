# Generated by Django 4.0.4 on 2022-06-20 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0009_remove_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
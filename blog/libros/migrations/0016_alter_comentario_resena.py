# Generated by Django 4.0.4 on 2022-06-22 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0015_alter_comentario_resena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='resena',
            field=models.IntegerField(verbose_name='Resena'),
        ),
    ]
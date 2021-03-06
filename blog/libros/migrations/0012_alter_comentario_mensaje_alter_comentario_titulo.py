# Generated by Django 4.0.4 on 2022-06-20 17:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0011_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='mensaje',
            field=ckeditor.fields.RichTextField(verbose_name='Mensaje'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='Título del Comentario'),
        ),
    ]

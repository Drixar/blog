# Generated by Django 4.0.4 on 2022-06-21 00:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0012_alter_comentario_mensaje_alter_comentario_titulo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
        migrations.AlterField(
            model_name='comentario',
            name='mensaje',
            field=ckeditor.fields.RichTextField(max_length=50, verbose_name='Mensaje'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.CharField(max_length=50, verbose_name='Usuario'),
        ),
    ]

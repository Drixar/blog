# Generated by Django 4.0.4 on 2022-06-16 20:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0005_alter_contacto_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='biografia',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Biografía'),
        ),
        migrations.AlterField(
            model_name='resena',
            name='contenido',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-20 14:38

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libros', '0010_categoria_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50, unique=True, verbose_name='Título del Comentario')),
                ('mensaje', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Mensaje')),
                ('estado', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('fecha_alta', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('resena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libros.resena')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Resena',
                'verbose_name_plural': 'Resenas',
            },
        ),
    ]

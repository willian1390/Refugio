# Generated by Django 4.2.9 on 2024-08-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicar_mas',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='contenido_blog',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='creado_blog',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de publicación'),
        ),
        migrations.AlterField(
            model_name='publicar_mas',
            name='descripcion_pubm',
            field=models.TextField(verbose_name='Descripción de la mascota'),
        ),
        migrations.AlterField(
            model_name='publicar_mas',
            name='fecha_pubm',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de publicación'),
        ),
    ]

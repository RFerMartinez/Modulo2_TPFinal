# Generated by Django 5.0.6 on 2024-06-15 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_categoria_fecha_creacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='activo',
            new_name='es_activo',
        ),
    ]

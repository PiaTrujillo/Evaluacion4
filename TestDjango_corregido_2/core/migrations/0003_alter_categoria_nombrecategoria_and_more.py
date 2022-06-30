# Generated by Django 4.0.5 on 2022-06-29 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto_archivo_alter_producto_precio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombreCategoria',
            field=models.CharField(max_length=50, verbose_name='Nombre categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=40, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='sku',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='sku'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(verbose_name='Stock'),
        ),
    ]
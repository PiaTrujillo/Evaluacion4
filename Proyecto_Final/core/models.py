from django.db import models

# Create your models here.

#Categoría del Producto
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre categoria")

    def __str__(self):
        return self.nombreCategoria

#Producto
class Producto(models.Model):
    sku = models.IntegerField(primary_key=True, verbose_name='sku')
    dv = models.CharField(max_length=1, verbose_name='dv') #se agrega
    nombre = models.CharField(max_length=40, verbose_name='Nombres') 
    primer_apellido = models.CharField(max_length=40, verbose_name='Primer Apellido') #se agrega
    segundo_apellido = models.CharField(max_length=40, verbose_name='Segundo Apellido') #se agrega
    precio = models.IntegerField(verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Stock')
    descripcion = models.CharField(max_length=100, null=True, blank=True, verbose_name='descripcion')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.sku
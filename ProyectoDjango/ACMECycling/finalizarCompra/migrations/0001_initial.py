# Generated by Django 3.0 on 2022-12-07 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('dir', models.CharField(blank=True, max_length=250)),
                ('creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('pagado', models.BooleanField(default=False)),
                ('estado', models.CharField(choices=[('Transito', 'Transito'), ('Pendiente', 'Pendiente'), ('Enviado', 'Enviado'), ('Recibido', 'Recibido')], default='Pendiente', max_length=1200)),
                ('metodoPago', models.CharField(choices=[('CR', 'Contrareembolso'), ('TJ', 'Tarjeta')], default='CR', max_length=2)),
                ('metodoEnvio', models.CharField(choices=[('CO', 'Correo'), ('SE', 'Seur')], default='CO', max_length=2)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('cliente', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-creacion',),
            },
        ),
        migrations.CreateModel(
            name='cantidadVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalizarCompra.Venta')),
            ],
        ),
    ]

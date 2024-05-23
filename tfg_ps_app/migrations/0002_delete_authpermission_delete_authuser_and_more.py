# Generated by Django 5.0.4 on 2024-05-23 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfg_ps_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.AlterModelOptions(
            name='inventario',
            options={'verbose_name': 'inventario', 'verbose_name_plural': 'inventarios'},
        ),
        migrations.AlterModelOptions(
            name='jugadores',
            options={'verbose_name': 'jugador', 'verbose_name_plural': 'jugadores'},
        ),
        migrations.AlterModelOptions(
            name='objetos',
            options={'verbose_name': 'objeto', 'verbose_name_plural': 'objetos'},
        ),
    ]

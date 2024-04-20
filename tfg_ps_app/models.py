from django.db import models


# Create your models here.
class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type_id", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user_id", "permission_id"),)


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class Inventario(models.Model):
    jugador_id = models.IntegerField(blank=True, null=True)
    objeto_id = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "inventario"
        unique_together = (("jugador_id", "objeto_id"),)


class Jugadores(models.Model):
    dinero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jugadores'


class Objetos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
    tipo_objeto = models.CharField(max_length=8, blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "objetos"

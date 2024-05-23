from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Jugadores, Objetos, Inventario

# OJO:
# Para ejecutar el TestCase de Django y trabajar con los datos existentes en la base de datos sin limpiarla, 
# puedes usar una configuración de pruebas un poco diferente. Los TestCase de Django, por defecto, usan una 
# base de datos en memoria que se resetea para cada test. Para evitar esto, puedes usar TransactionTestCase y setUpTestData,
# que no reinician la base de datos entre tests.
# Sin embargo, para asegurarte de que los objetos de la tienda ya están en la base de datos y no deseas 
# crearlos en el test, puedes modificar el test de la siguiente manera:

# Eliminar la creación de objetos en setUp.
# Asegurarte de que los objetos ya existen en la base de datos antes de ejecutar el test.


class TiendaTestCase01(TestCase):
    def setUp(self):
        # Crear un usuario para las pruebas
        self.user = User.objects.create_user(
            username="test_user", password="test_password"
        )
        # Crear un jugador asociado al usuario
        self.jugador = Jugadores.objects.create(user=self.user)
        # Crear algunos objetos para la tienda
        self.objeto_1 = Objetos.objects.create(nombre="Objeto1", precio=100)
        self.objeto_2 = Objetos.objects.create(nombre="Objeto2", precio=200)

    def test_compra_venta_tienda(self):
        # Iniciar sesión como el usuario creado
        self.client.login(username="test_user", password="test_password")

        # Comprar un objeto en la tienda
        response = self.client.post(
            reverse("tfg_ps_app:comprar_objeto", args=[self.objeto_1.pk])
        )
        self.assertEqual(
            response.status_code, 302
        )  # Debería redirigir a la página de la tienda
        # Verificar que el objeto se haya agregado al inventario del jugador
        inventario_objeto_1 = Inventario.objects.get(
            jugador=self.jugador, objeto=self.objeto_1
        )
        self.assertEqual(inventario_objeto_1.cantidad, 1)

        # Vender el objeto comprado
        response = self.client.post(
            reverse("tfg_ps_app:vender_objeto", args=[inventario_objeto_1.pk])
        )
        self.assertEqual(
            response.status_code, 302
        )  # Debería redirigir a la página de la tienda
        # Verificar que el objeto se haya eliminado del inventario del jugador
        with self.assertRaises(Inventario.DoesNotExist):
            Inventario.objects.get(jugador=self.jugador, objeto=self.objeto_1)

        # Comprar otro objeto en la tienda
        response = self.client.post(
            reverse("tfg_ps_app:comprar_objeto", args=[self.objeto_2.pk])
        )
        self.assertEqual(
            response.status_code, 302
        )  # Debería redirigir a la página de la tienda
        # Verificar que el segundo objeto se haya agregado al inventario del jugador
        inventario_objeto_2 = Inventario.objects.get(
            jugador=self.jugador, objeto=self.objeto_2
        )
        self.assertEqual(inventario_objeto_2.cantidad, 1)

        # Cerrar sesión
        self.client.logout()

    def test_ver_inventario(self):
        # Iniciar sesión como el usuario creado
        self.client.login(username="test_user", password="test_password")

        # Comprar un objeto en la tienda
        self.client.post(reverse("tfg_ps_app:comprar_objeto", args=[self.objeto_1.pk]))

        # Acceder al inventario del jugador
        response = self.client.get(reverse("tfg_ps_app:tienda"))
        self.assertEqual(
            response.status_code, 200
        )  # Debería devolver un código de éxito
        self.assertContains(
            response, "Objeto1"
        )  # Debería mostrar el objeto comprado en el inventario

        # Cerrar sesión
        self.client.logout()


class TiendaTestCase02(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Asumiendo que los objetos ya existen en la base de datos
        cls.objeto_1 = Objetos.objects.get(nombre="Objeto1")
        cls.objeto_2 = Objetos.objects.get(nombre="Objeto2")

    def test_registro_inicio_compra_venta_inventario_cierre(self):
        # Registro de un nuevo usuario
        user_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "test_password",
        }
        response = self.client.post(reverse("tfg_ps_app:signup"), data=user_data)
        self.assertEqual(
            response.status_code, 302
        )  # Debería redirigir a la página de inicio o tienda

        # Obtener el usuario y crear un jugador asociado
        self.user = User.objects.get(username="test_user")
        self.jugador = Jugadores.objects.get(user=self.user)

        # Iniciar sesión como el usuario registrado
        self.client.login(username="test_user", password="test_password")

        # Comprar un objeto en la tienda
        response = self.client.post(
            reverse("tfg_ps_app:comprar_objeto", args=[self.objeto_1.pk])
        )
        self.assertEqual(
            response.status_code, 302
        )  # Debería redirigir a la página de la tienda
        # Verificar que el objeto se haya agregado al inventario del jugador
        inventario_objeto_1 = Inventario.objects.get(
            jugador=self.jugador, objeto=self.objeto_1
        )
        self.assertEqual(inventario_objeto_1.cantidad, 1)

        # Ver el inventario del jugador
        response = self.client.get(reverse("tfg_ps_app:tienda"))
        self.assertEqual(
            response.status_code, 200
        )  # Debería devolver un código de éxito
        self.assertContains(
            response, "Objeto1"
        )  # Debería mostrar el objeto comprado en el inventario

        # Vender el objeto comprado
        response = self.client.post(
            reverse("tfg_ps_app:vender_objeto", args=[inventario_objeto_1.pk])
        )
        self.assertEqual(
            response.status_code, 302
        )  # Debería redirigir a la página de la tienda
        # Verificar que el objeto se haya eliminado del inventario del jugador
        with self.assertRaises(Inventario.DoesNotExist):
            Inventario.objects.get(jugador=self.jugador, objeto=self.objeto_1)

        # Ver el inventario del jugador después de la venta
        response = self.client.get(reverse("tfg_ps_app:tienda"))
        self.assertEqual(
            response.status_code, 200
        )  # Debería devolver un código de éxito
        self.assertNotContains(
            response, "Objeto1"
        )  # No debería mostrar el objeto vendido en el inventario

        # Comprar otro objeto en la tienda
        response = self.client.post(
            reverse("tfg_ps_app:comprar_objeto", args=[self.objeto_2.pk])
        )
        self.assertEqual(
            response.status_code, 302
        )  # Debería redirigir a la página de la tienda
        # Verificar que el segundo objeto se haya agregado al inventario del jugador
        inventario_objeto_2 = Inventario.objects.get(
            jugador=self.jugador, objeto=self.objeto_2
        )
        self.assertEqual(inventario_objeto_2.cantidad, 1)

        # Ver el detalle del segundo objeto
        response = self.client.get(
            reverse("tfg_ps_app:detalle_objeto", args=[self.objeto_2.pk])
        )
        self.assertEqual(
            response.status_code, 200
        )  # Debería devolver un código de éxito
        self.assertContains(
            response, "Objeto2"
        )  # Debería mostrar los detalles del segundo objeto

        # Cerrar sesión
        self.client.logout()

        # Verificar que el usuario ha cerrado sesión
        response = self.client.get(reverse("tfg_ps_app:tienda"))
        self.assertNotEqual(
            response.status_code, 200
        )  # No debería devolver un código de éxito sin iniciar sesión

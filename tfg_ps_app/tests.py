from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Jugadores, Objetos, Inventario

class TiendaTestCase(TestCase):
    def setUp(self):
        # Crear un usuario para las pruebas
        self.user = User.objects.create_user(username="test_user", password="test_password")
        # Crear un jugador asociado al usuario con suficiente dinero
        self.jugador = Jugadores.objects.create(user=self.user, dinero=500)
        # Crear algunos objetos para la tienda
        self.objeto_1 = Objetos.objects.create(nombre="Objeto1", descripcion="Descripción del Objeto1", precio=100, tipo_objeto="Tipo1")
        self.objeto_2 = Objetos.objects.create(nombre="Objeto2", descripcion="Descripción del Objeto2", precio=200, tipo_objeto="Tipo2")

    def test_login_signup(self):
        # Registro de un nuevo usuario
        user_data = {
            "username": "new_test_user",
            "password1": "new_test_password",
            "password2": "new_test_password",
        }
        response = self.client.post(reverse("tfg_ps_app:signup"), data=user_data)
        self.assertEqual(response.status_code, 302)  # Debería redirigir a la página de inicio

        # Iniciar sesión como el nuevo usuario registrado
        self.client.login(username="new_test_user", password="new_test_password")
        response = self.client.get(reverse("tfg_ps_app:inicio"))
        self.assertEqual(response.status_code, 200)  # La página de inicio debería cargarse correctamente
        self.client.logout()

    def test_compra_venta_tienda(self):
        # Iniciar sesión como el usuario creado
        self.client.login(username="test_user", password="test_password")

        # Comprar un objeto en la tienda
        response = self.client.post(reverse("tfg_ps_app:comprar_objeto", args=[self.objeto_1.pk]))
        self.assertEqual(response.status_code, 302)  # Debería redirigir a la página de la tienda

        # Verificar que el objeto se haya agregado al inventario del jugador
        inventario_objeto_1 = Inventario.objects.get(jugador=self.jugador, objeto=self.objeto_1)
        self.assertEqual(inventario_objeto_1.cantidad, 1)

        # Verificar que el dinero del jugador se haya reducido correctamente
        self.jugador.refresh_from_db()
        self.assertEqual(self.jugador.dinero, 400)

        # Vender el objeto comprado
        response = self.client.post(reverse("tfg_ps_app:vender_objeto", args=[inventario_objeto_1.pk]))
        self.assertEqual(response.status_code, 302)  # Debería redirigir a la página de la tienda

        # Verificar que el objeto se haya eliminado del inventario del jugador
        with self.assertRaises(Inventario.DoesNotExist):
            Inventario.objects.get(jugador=self.jugador, objeto=self.objeto_1)

        # Verificar que el dinero del jugador se haya incrementado correctamente
        self.jugador.refresh_from_db()
        self.assertEqual(self.jugador.dinero, 500)

        # Comprar otro objeto en la tienda
        response = self.client.post(reverse("tfg_ps_app:comprar_objeto", args=[self.objeto_2.pk]))
        self.assertEqual(response.status_code, 302)  # Debería redirigir a la página de la tienda

        # Verificar que el segundo objeto se haya agregado al inventario del jugador
        inventario_objeto_2 = Inventario.objects.get(jugador=self.jugador, objeto=self.objeto_2)
        self.assertEqual(inventario_objeto_2.cantidad, 1)

        # Verificar que el dinero del jugador se haya reducido correctamente
        self.jugador.refresh_from_db()
        self.assertEqual(self.jugador.dinero, 300)

        # Cerrar sesión
        self.client.logout()

    def test_ver_inventario(self):
        # Iniciar sesión como el usuario creado
        self.client.login(username="test_user", password="test_password")

        # Comprar un objeto en la tienda
        self.client.post(reverse("tfg_ps_app:comprar_objeto", args=[self.objeto_1.pk]))

        # Acceder al inventario del jugador
        response = self.client.get(reverse("tfg_ps_app:tienda"))
        self.assertEqual(response.status_code, 200)  # La página de la tienda debería cargarse correctamente
        self.assertContains(response, "Objeto1")  # La página debería mostrar el objeto comprado en el inventario

        # Cerrar sesión
        self.client.logout()

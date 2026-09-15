from django.test import TestCase
from django.urls import reverse

class CatalogoViewsTests(TestCase):
    def test_lista_view(self):
        response = self.client.get(reverse('catalogo:lista'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Catálogo de Productos Tecnológicos')
        self.assertContains(response, 'Benjamín Rivas')

    def test_detalle_view(self):
        response = self.client.get(reverse('catalogo:detalle'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Detalle de Producto')
        self.assertContains(response, 'Laptop Developer Pro 16')


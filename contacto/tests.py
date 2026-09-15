from django.test import TestCase
from django.urls import reverse

class ContactoViewsTests(TestCase):
    def test_formulario_get(self):
        response = self.client.get(reverse('contacto:formulario'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Centro de Contacto & Asistencia Técnica')
        self.assertContains(response, 'Benjamín Rivas')

    def test_formulario_post(self):
        response = self.client.post(reverse('contacto:formulario'), {
            'nombre': 'Benjamín Rivas',
            'email': 'benjamin@example.com',
            'tipo': 'soporte',
            'asunto': 'Consulta técnica',
            'mensaje': 'Mensaje de prueba para evaluación'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '¡Mensaje Enviado con Éxito!')

    def test_faq_view(self):
        response = self.client.get(reverse('contacto:faq'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Preguntas Frecuentes (FAQ)')
        self.assertContains(response, '¿Cuáles son los tiempos estimados de despacho a regiones?')


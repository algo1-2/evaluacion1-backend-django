from django.shortcuts import render

def formulario(request):
    """Vista 1 de la app contacto: Formulario y canales de soporte"""
    enviado = False
    if request.method == 'POST':
        enviado = True
    return render(request, 'contacto/formulario.html', {'enviado': enviado})

def faq(request):
    """Vista 2 de la app contacto: Preguntas frecuentes con acordeón interactivo"""
    faqs = [
        {
            'pregunta': '¿Cuáles son los tiempos estimados de despacho a regiones?',
            'respuesta': 'Para la Región Metropolitana los envíos tardan de 24 a 48 horas hábiles. Para otras regiones de Chile, el plazo estándar es de 3 a 5 días hábiles mediante transporte certificado.',
            'icono': 'bi-truck'
        },
        {
            'pregunta': '¿Qué cobertura y plazo ofrece la garantía técnica?',
            'respuesta': 'Todos los equipos y componentes cuentan con 6 meses de garantía legal y hasta 2 o 3 años de garantía extendida de fábrica ante fallas de fabricación.',
            'icono': 'bi-shield-check'
        },
        {
            'pregunta': '¿Emiten factura para empresas y personas jurídicas?',
            'respuesta': 'Sí, al momento de realizar la cotización o compra puedes indicar tu RUT de empresa y giro comercial para la emisión inmediata de factura electrónica.',
            'icono': 'bi-receipt'
        },
        {
            'pregunta': '¿Qué medios de pago aceptan?',
            'respuesta': 'Aceptamos transferencias bancarias directas, tarjetas de débito/crédito a través de Webpay Plus, Mercado Pago y órdenes de compra institucionales.',
            'icono': 'bi-credit-card'
        },
        {
            'pregunta': '¿Ofrecen servicio de armado y testeo de componentes?',
            'respuesta': 'Sí, disponemos de servicio técnico especializado para el ensamblado, instalación de sistema operativo y pruebas de estrés de 24 horas antes de la entrega.',
            'icono': 'bi-tools'
        }
    ]
    return render(request, 'contacto/faq.html', {'faqs': faqs})

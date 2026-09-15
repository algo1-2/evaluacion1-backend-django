from django.shortcuts import render

def lista(request):
    """Vista 1 de la app catalogo: Lista general de productos"""
    productos = [
        {
            'id': 1,
            'nombre': 'Laptop Developer Pro 16"',
            'categoria': 'Laptops',
            'descripcion': 'Procesador Intel i7 13ª Gen, 32GB RAM DDR5, 1TB SSD NVMe, Pantalla 2K.',
            'precio': '1.299.990',
            'stock': 8,
            'calificacion': '4.8',
            'icono': 'bi-laptop'
        },
        {
            'id': 2,
            'nombre': 'Monitor UltraWide 34" Curvo',
            'categoria': 'Monitores',
            'descripcion': 'Resolución WQHD 144Hz, 1ms, HDR400, panel IPS con soporte ergonómico.',
            'precio': '489.990',
            'stock': 12,
            'calificacion': '4.7',
            'icono': 'bi-display'
        },
        {
            'id': 3,
            'nombre': 'Teclado Mecánico Custom RGB',
            'categoria': 'Periféricos',
            'descripcion': 'Switches Red lubricados, conexión inalámbrica 2.4GHz y Bluetooth, teclas PBT.',
            'precio': '89.990',
            'stock': 25,
            'calificacion': '4.9',
            'icono': 'bi-keyboard'
        },
        {
            'id': 4,
            'nombre': 'Tarjeta Gráfica RTX 4070 Ti',
            'categoria': 'Componentes',
            'descripcion': '12GB GDDR6X, refrigeración triple ventilador, ideal para IA y render 3D.',
            'precio': '849.990',
            'stock': 4,
            'calificacion': '5.0',
            'icono': 'bi-gpu-card'
        },
        {
            'id': 5,
            'nombre': 'Servidor NAS 4 Bahías 32TB',
            'categoria': 'Almacenamiento',
            'descripcion': 'Almacenamiento redundante para backups de código y bases de datos en red.',
            'precio': '620.000',
            'stock': 0,
            'calificacion': '4.6',
            'icono': 'bi-hdd-network'
        },
        {
            'id': 6,
            'nombre': 'Mouse Ergonómico Vertical',
            'categoria': 'Periféricos',
            'descripcion': 'Diseñado para reducir fatiga postural en sesiones prolongadas de programación.',
            'precio': '42.990',
            'stock': 19,
            'calificacion': '4.5',
            'icono': 'bi-mouse'
        }
    ]
    return render(request, 'catalogo/lista.html', {'productos': productos})

def detalle(request):
    """Vista 2 de la app catalogo: Detalle técnico de un producto"""
    producto = {
        'nombre': 'Laptop Developer Pro 16" - Edición 2026',
        'precio': '1.299.990',
        'descripcion_larga': 'La herramienta definitiva para ingenieros de software, analistas de datos y desarrolladores backend. Diseñada con un chasis de aluminio de grado aeronáutico, batería de larga duración de 99Wh y un sistema de enfriamiento de cámara de vapor para cargas de compilación intensas.',
        'especificaciones': [
            {'clave': 'Procesador', 'valor': 'Intel Core i7-13700H (14 núcleos, hasta 5.0 GHz)'},
            {'clave': 'Memoria RAM', 'valor': '32 GB DDR5 5200MHz (expandible a 64 GB)'},
            {'clave': 'Almacenamiento', 'valor': '1 TB SSD M.2 NVMe PCIe 4.0 (ranura secundaria libre)'},
            {'clave': 'Pantalla', 'valor': '16" IPS WQXGA (2560 x 1600), 165Hz, 100% sRGB'},
            {'clave': 'Conectividad', 'valor': 'Wi-Fi 6E, Bluetooth 5.3, Thunderbolt 4, HDMI 2.1, RJ-45 Gigabit'},
            {'clave': 'Sistema Operativo', 'valor': 'Ubuntu Linux / Windows 11 Pro compatible'}
        ]
    }
    return render(request, 'catalogo/detalle.html', {'producto': producto})

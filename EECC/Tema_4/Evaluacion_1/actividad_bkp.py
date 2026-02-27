# =========================
# ACTIVIDAD POR PAREJAS
# Built-ins + lambda + recursividad
# Entrega: actividad.py
# =========================

# --- DATOS (NO TOCAR) ---
tienda = {
    "iva": 0.21,
    "nombre": "TechTrassierra",
    "clientes": {
        "C1": {"nombre": "Ana", "nivel": "gold", "provincia": "Córdoba"},
        "C2": {"nombre": "Luis", "nivel": "basic", "provincia": "Sevilla"},
        "C3": {"nombre": "Marta", "nivel": "silver", "provincia": "Córdoba"},
        "C4": {"nombre": "Ibrahim", "nivel": "basic", "provincia": "Jaén"},
        "C5": {"nombre": "Gloria", "nivel": "gold", "provincia": "Málaga"},
        "C6": {"nombre": "Pablo", "nivel": "silver", "provincia": "Cádiz"},
    },
    "productos": {
        "P101": {"nombre": "Teclado Mecánico", "precio": 59.90, "categoria": "perifericos/entrada", "stock": 8, "activo": True},
        "P102": {"nombre": "Ratón Gaming", "precio": 24.50, "categoria": "perifericos/entrada", "stock": 15, "activo": True},
        "P103": {"nombre": "Monitor 24\"", "precio": 129.99, "categoria": "pantallas/monitores", "stock": 4, "activo": True},
        "P104": {"nombre": "HDMI 2m", "precio": 7.00, "categoria": "cables/video", "stock": 50, "activo": True},
        "P105": {"nombre": "USB-C 1m", "precio": 9.50, "categoria": "cables/datos", "stock": 35, "activo": True},
        "P106": {"nombre": "Auriculares In-Ear", "precio": 19.99, "categoria": "audio/auriculares", "stock": 0, "activo": True},
        "P107": {"nombre": "Altavoz Bluetooth", "precio": 39.90, "categoria": "audio/altavoces", "stock": 6, "activo": True},
        "P108": {"nombre": "SSD 1TB", "precio": 74.90, "categoria": "almacenamiento/ssd", "stock": 9, "activo": True},
        "P109": {"nombre": "Pendrive 128GB", "precio": 12.99, "categoria": "almacenamiento/usb", "stock": 20, "activo": True},
        "P110": {"nombre": "Webcam 1080p", "precio": 34.95, "categoria": "perifericos/camara", "stock": 7, "activo": True},
        "P111": {"nombre": "Router WiFi 6", "precio": 89.00, "categoria": "red/router", "stock": 3, "activo": True},
        "P112": {"nombre": "Switch 8 puertos", "precio": 22.00, "categoria": "red/switch", "stock": 10, "activo": True},
    },
    "pedidos": [
        {"id": 1001, "cliente_id": "C1", "pagado": True,  "cupon": 0.10, "fecha": "2026-02-10", "envio": {"tipo": "standard", "coste": 3.99},
         "items": [{"sku": "P101", "qty": 1}, {"sku": "P104", "qty": 2}]},
        {"id": 1002, "cliente_id": "C2", "pagado": False, "cupon": 0.00, "fecha": "2026-02-11", "envio": {"tipo": "standard", "coste": 3.99},
         "items": [{"sku": "P103", "qty": 1}, {"sku": "P102", "qty": 1}]},
        {"id": 1003, "cliente_id": "C3", "pagado": True,  "cupon": 0.00, "fecha": "2026-02-12", "envio": {"tipo": "express", "coste": 6.99},
         "items": [{"sku": "P102", "qty": 3}, {"sku": "P105", "qty": 1}]},
        {"id": 1004, "cliente_id": "C1", "pagado": True,  "cupon": 0.05, "fecha": "2026-02-13", "envio": {"tipo": "standard", "coste": 3.99},
         "items": [{"sku": "P103", "qty": 1}, {"sku": "P104", "qty": 1}]},
        {"id": 1005, "cliente_id": "C4", "pagado": True,  "cupon": 0.00, "fecha": "2026-02-14", "envio": {"tipo": "pickup", "coste": 0.00},
         "items": [{"sku": "P112", "qty": 1}, {"sku": "P105", "qty": 2}]},
        {"id": 1006, "cliente_id": "C5", "pagado": True,  "cupon": 0.15, "fecha": "2026-02-15", "envio": {"tipo": "express", "coste": 6.99},
         "items": [{"sku": "P108", "qty": 1}, {"sku": "P109", "qty": 2}]},
        {"id": 1007, "cliente_id": "C6", "pagado": False, "cupon": 0.00, "fecha": "2026-02-16", "envio": {"tipo": "standard", "coste": 3.99},
         "items": [{"sku": "P111", "qty": 1}]},
        {"id": 1008, "cliente_id": "C2", "pagado": True,  "cupon": 0.05, "fecha": "2026-02-17", "envio": {"tipo": "pickup", "coste": 0.00},
         "items": [{"sku": "P110", "qty": 1}, {"sku": "P107", "qty": 1}]},
    ],
}

catalogo = {
    "nombre": "tienda",
    "hijos": [
        {"nombre": "perifericos", "hijos": [
            {"nombre": "entrada", "hijos": [
                {"nombre": "Teclado Mecánico", "sku": "P101", "precio": 59.90},
                {"nombre": "Ratón Gaming", "sku": "P102", "precio": 24.50},
            ]},
            {"nombre": "camara", "hijos": [
                {"nombre": "Webcam 1080p", "sku": "P110", "precio": 34.95},
            ]},
            {"nombre": "impresion", "hijos": []},
        ]},
        {"nombre": "pantallas", "hijos": [
            {"nombre": "monitores", "hijos": [
                {"nombre": "Monitor 24\"", "sku": "P103", "precio": 129.99},
            ]}
        ]},
        {"nombre": "cables", "hijos": [
            {"nombre": "video", "hijos": [
                {"nombre": "HDMI 2m", "sku": "P104", "precio": 7.00},
            ]},
            {"nombre": "datos", "hijos": [
                {"nombre": "USB-C 1m", "sku": "P105", "precio": 9.50},
            ]},
        ]},
        {"nombre": "audio", "hijos": [
            {"nombre": "auriculares", "hijos": [
                {"nombre": "Auriculares In-Ear", "sku": "P106", "precio": 19.99},
            ]},
            {"nombre": "altavoces", "hijos": [
                {"nombre": "Altavoz Bluetooth", "sku": "P107", "precio": 39.90},
            ]},
        ]},
        {"nombre": "almacenamiento", "hijos": [
            {"nombre": "ssd", "hijos": [
                {"nombre": "SSD 1TB", "sku": "P108", "precio": 74.90},
            ]},
            {"nombre": "usb", "hijos": [
                {"nombre": "Pendrive 128GB", "sku": "P109", "precio": 12.99},
            ]},
        ]},
        {"nombre": "red", "hijos": [
            {"nombre": "router", "hijos": [
                {"nombre": "Router WiFi 6", "sku": "P111", "precio": 89.00},
            ]},
            {"nombre": "switch", "hijos": [
                {"nombre": "Switch 8 puertos", "sku": "P112", "precio": 22.00},
            ]},
        ]},
    ],
}

# --- PLANTILLA (COMPLETAR TODOs) ---

def subtotal_pedido_map(pedido, tienda):
    """
    OBLIGATORIO: debe devolver sum(map(...))
    Subtotal = suma de (precio * qty) de todos los items.
    """
    
    pass


def unidades_totales_sku(tienda, sku):
    """Unidades totales pedidas de ese SKU SOLO en pedidos pagados."""
    
    pass


def skus_con_stock_insuficiente(tienda):
    """
    SKUs cuyo total de unidades pedidas (pagadas) supera su stock.
    OBLIGATORIO: usar filter(lambda ...) en esta función.
    """
    
    pass


def ranking_clientes_pagados(tienda):
    """
    Lista (cliente_id, gasto_total) solo pagados, ordenada desc por gasto.
    OBLIGATORIO: usar sorted(..., key=lambda ..., reverse=True)
    """
    
    pass


def hay_producto_agotado_en_pedidos_pagados(tienda):
    """
    True si algún pedido pagado contiene producto con stock == 0.
    OBLIGATORIO: usar any(...)
    """
    
    pass


def profundidad_maxima(nodo):
    """RECURSIVA: profundidad máxima del árbol. Raíz = 1."""
    
    pass


def contar_categorias(nodo):
    """RECURSIVA: cuenta nodos que tienen clave 'hijos' (categorías)."""
    
    pass


if __name__ == "__main__":
    print("--- PRUEBAS ---")

    print("Subtotal primer pedido:", round(subtotal_pedido_map(tienda["pedidos"][0], tienda), 2))
    print("Unidades pagadas de P103:", unidades_totales_sku(tienda, "P103"))
    print("SKUs con stock insuficiente:", skus_con_stock_insuficiente(tienda))

    ranking = ranking_clientes_pagados(tienda)
    print("Ranking clientes (top 3):", ranking[:3])

    print("¿Hay producto agotado en pedidos pagados?:", hay_producto_agotado_en_pedidos_pagados(tienda))
    print("Profundidad máxima del catálogo:", profundidad_maxima(catalogo))
    print("Número de categorías:", contar_categorias(catalogo))
pedidos = [
    {"id":101, "cliente":"Ana", "importe":29.9, "pagado": True},
    {"id":102, "cliente":"Pepe", "importe":4.6, "pagado": False},
    {"id":103, "cliente":"Ana", "importe":200.6, "pagado": False},
    {"id":104, "cliente":"Pepe", "importe":49.6, "pagado": False},
    {"id":105, "cliente":"Sara", "importe":75.6, "pagado": False}
]

# x = filter(lambda x:x["pagado"]==True,pedidos)

# print(list(x))

# x = filter(lambda x:x["importe"]>=100,pedidos)
# print("caros: ",list(x))

# lprint(list(x))
# exit()


# print(pedidos[0]["importe"])
iterador = map(lambda x:x["importe"],pedidos)
print(list(iterador))

iterador = map(lambda x:(x["cliente"],x["importe"]), pedidos)
print(list(iterador))

print(pedidos[0]["importe"])

sacar_importe = lambda x: x["id"]
print(sacar_importe(pedidos[0]))

pedidos_ordenados = sorted(pedidos, key=lambda p: p["importe"])
print(pedidos_ordenados)
print("maximo: ",pedidos_ordenados[0])
print("minimo: ",pedidos_ordenados[-1])

pedido_cli_imp = sorted(pedidos, key=lambda p: (p["cliente"], p["importe"]))

for i in pedido_cli_imp:
    print(i)



aplicar_descuento = lambda importe, porcentaje: importe *(1-porcentaje/100)
precio_final = aplicar_descuento(200, 10)
print(precio_final)

calcular_iva = lambda importe=100, iva=0.21: round(importe*(1+iva), 2)

print(calcular_iva())
print(calcular_iva(8))
print(calcular_iva(8,0.4))
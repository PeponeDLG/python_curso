from datetime import datetime, date, time

# Fecha y hora actual
ahora = datetime.datetime.now()
print("Fecha y hora actual:", ahora)
print("Solo fecha:", ahora.date())
print("Solo hora:", ahora.time())

# Fecha actual (sin hora)
hoy = date.today()
print("Hoy es:", hoy)


# Crear una fecha específica
fecha1 = date(2024, 3, 15)  # Año, Mes, Día
print("Fecha específica:", fecha1)

# Crear una fecha con hora
fecha_hora1 = datetime(2024, 3, 15, 14, 30, 45)  # Año, Mes, Día, Hora, Minuto, Segundo
print("Fecha y hora específica:", fecha_hora1)

# Crear solo hora
hora1 = time(14, 30, 45)  # Hora, Minuto, Segundo
print("Hora específica:", hora1)

# Formatear fechas

ahora = datetime.now()

# Formatear fecha a string
print("Fecha formateada:", ahora.strftime("%d/%m/%Y"))           # 15/03/2024
print("Fecha completa:", ahora.strftime("%A %d de %B del %Y"))   # Viernes 15 de Marzo del 2024
print("Hora formateada:", ahora.strftime("%H:%M:%S"))            # 14:30:45

# Formatos comunes:
print("\n=== FORMATOS COMUNES ===")
print("ISO:", ahora.isoformat())                     # 2024-03-15T14:30:45.123456
print("YYYY-MM-DD:", ahora.strftime("%Y-%m-%d"))     # 2024-03-15
print("DD/MM/YYYY:", ahora.strftime("%d/%m/%Y"))     # 15/03/2024
print("MM/DD/YYYY:", ahora.strftime("%m/%d/%Y"))     # 03/15/2024
print("HH:MM:SS:", ahora.strftime("%H:%M:%S"))       # 14:30:45
print("HH:MM AM/PM:", ahora.strftime("%I:%M %p"))    # 02:30 PM

# Convertir string a fecha

# Convertir string a datetime
texto_fecha = "15/03/2024 14:30:45"
fecha_obj = datetime.strptime(texto_fecha, "%d/%m/%Y %H:%M:%S")
print("String convertido a datetime:", fecha_obj)

# Diferentes formatos de entrada
formato1 = "2024-03-15"
fecha1 = datetime.strptime(formato1, "%Y-%m-%d")

formato2 = "15 March, 2024"
fecha2 = datetime.strptime(formato2, "%d %B, %Y")

formato3 = "03/15/24 02:30PM"
fecha3 = datetime.strptime(formato3, "%m/%d/%y %I:%M%p")

# Operaciones con fechas

hoy = datetime.now()

# Sumar días
futuro = hoy + timedelta(days=7)
print("En 7 días:", futuro)

# Restar días
pasado = hoy - timedelta(days=30)
print("Hace 30 días:", pasado)

# Operaciones complejas
fecha_modificada = hoy + timedelta(days=5, hours=3, minutes=30, seconds=45)
print("Dentro de 5 días, 3h, 30m, 45s:", fecha_modificada)

# Diferencia entre fechas
fecha1 = datetime(2024, 3, 1)
fecha2 = datetime(2024, 3, 15)
diferencia = fecha2 - fecha1
print("\nDiferencia entre fechas:", diferencia)
print("Días de diferencia:", diferencia.days)
print("Segundos totales:", diferencia.total_seconds())

# Extraer componentes de fechas

ahora = datetime.now()

print("Año:", ahora.year)
print("Mes:", ahora.month)
print("Día:", ahora.day)
print("Hora:", ahora.hour)
print("Minuto:", ahora.minute)
print("Segundo:", ahora.second)
print("Microsegundo:", ahora.microsecond)

# Día de la semana (0=lunes, 6=domingo)
print("Día de la semana (número):", ahora.weekday())
print("Día de la semana (nombre):", ahora.strftime("%A"))

# Día del año
print("Día del año:", ahora.timetuple().tm_yday)

# Comparar fechas

fecha1 = datetime(2024, 3, 15)
fecha2 = datetime(2024, 3, 20)

print("fecha1 < fecha2:", fecha1 < fecha2)   # True
print("fecha1 > fecha2:", fecha1 > fecha2)   # False
print("fecha1 == fecha2:", fecha1 == fecha2) # False

# Comparar solo fechas (ignorando hora)
hoy = date.today()
mañana = date(2024, 3, 16)
print("Hoy es antes que mañana:", hoy < mañana)
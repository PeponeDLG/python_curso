import pandas as pd
from ydata_profiling import ProfileReport

# Leer el archivo CSV
df = pd.read_csv("listings.csv")

# Generar el informe
profile = ProfileReport(df, title="Informe EDA Airbnb Barcelona", explorative=True)

# Exportar el informe a HTML
profile.to_file("reporte_airbnb_barcelona.html")

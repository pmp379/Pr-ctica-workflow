import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset CSV
data = pd.read_csv('players_stats.csv')

# Crear un gráfico de dispersión
plt.scatter(data['Height'], data['REB'], c='blue', label='players Data')
plt.xlabel('Height player (cm)')
plt.ylabel('Rebotes player')
plt.title('Altura vs rebotes capturados')
plt.legend()
plt.grid(True)

# Guardar el gráfico
plt.savefig('scatter_plot.png')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import os

# Crear carpeta para output
os.makedirs('/app/output', exist_ok=True)

# Generar señal senoidal
print("📈 Generando señal senoidal...")

x = np.linspace(0, 4 * np.pi, 1000)
y = np.sin(x)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='Sen(x)')
plt.title('Señal Senoidal 📊', fontsize=16)
plt.xlabel('Tiempo (radianes)', fontsize=12)
plt.ylabel('Amplitud', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

# Guardar gráfico
output_path = '/app/output/senoidal.png'
plt.savefig(output_path, dpi=100, bbox_inches='tight')
plt.close()

print(f"✅ Gráfico guardado en: {output_path}")

# Mostrar información del gráfico
print(f"\n📋 Información del gráfico:")
print(f"- Puntos: {len(x)}")
print(f"- Rango X: {x[0]:.2f} a {x[-1]:.2f}")
print(f"- Rango Y: {y.min():.2f} a {y.max():.2f}")

# Generar datos adicionales
print(f"\n🧮 Datos de muestra (primeros 5 puntos):")
for i in range(5):
    print(f"  x={x[i]:.3f}, y={y[i]:.3f}")